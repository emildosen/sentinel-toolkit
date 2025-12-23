# Emergency Access Account Sign-in

Alert when an emergency access (break-glass) account has been used. Run every 5 minutes with a 5-minute lookback.

## Purpose

Detects sign-ins from emergency access accounts which should only be used in break-glass scenarios. Any use should trigger immediate investigation.

## Configuration

Update the `EmergencyAccessAccounts` list with your organization's emergency account UPNs.

## Query

```kusto
let EmergencyAccessAccounts = dynamic(["emergencyaccess1@example.com", "emergencyaccess2@example.com"]);
SigninLogs
| where UserPrincipalName in~ (EmergencyAccessAccounts)
| project
    TimeGenerated,
    UserPrincipalName,
    UserId,
    IPAddress,
    Location = strcat(LocationDetails.city, ", ", LocationDetails.countryOrRegion),
    AppDisplayName,
    ResultType,
    ResultDescription,
    DeviceDetail,
    ConditionalAccessStatus
```
