
# SharePoint to OneDrive exfiltration

Alert when user copies or moves data from SharePoint to OneDrive.

## Purpose

Detects possible data exfiltration where user copies/moves data from SharePoint to a personal OneDrive.

## Query

```kusto
let threshold = 1;
let timeWindow = 1h;
OfficeActivity
| where TimeGenerated > ago(timeWindow)
| where Operation == "FileCopied"
| where OfficeWorkload == "OneDrive"
| extend SourceFileUrl = extract(@"<SourceFileUrl>([^<]+)</SourceFileUrl>", 1, Event_Data)
| where SourceFileUrl !contains "-my.sharepoint"  // source is a SharePoint site, not another OneDrive
| extend SourceSite = extract(@"https://[^/]+/sites/([^/]+)", 1, SourceFileUrl)
| summarize
    FileCount = count(),
    Files = make_set(OfficeObjectId),
    SourceSites = make_set(SourceSite),
    StartTime = min(TimeGenerated),
    EndTime = max(TimeGenerated)
    by UserId, bin(TimeGenerated, timeWindow)
| where FileCount >= threshold
```