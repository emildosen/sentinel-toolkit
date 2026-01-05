# Local Admin Sign-in

## Purpose
Review administrator sign-in events on devices.

## Query

```kusto
DeviceLogonEvents | where IsLocalAdmin == true | where LogonType == "Interactive"
| summarize count() by AccountName, DeviceName, AccountDomain | sort by count_ desc
```