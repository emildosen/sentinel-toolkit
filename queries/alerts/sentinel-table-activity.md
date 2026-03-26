# Sentinel Health Monitoring

Alert when key Sentinel tables goes dark. 

## Purpose

Detects when logging stops to key Sentinel tables.

## Configuration

Set to check the last 72 hours (change to fit your environment).

## Query

```kusto
union
    (OfficeActivity | summarize Count = count() | extend TableName = "OfficeActivity"),
    (SigninLogs | summarize Count = count() | extend TableName = "SigninLogs"),
    (AuditLogs | summarize Count = count() | extend TableName = "AuditLogs"),
    (SentinelHealth | summarize Count = count() | extend TableName = "SentinelHealth"),
    (ThreatIntelIndicators | summarize Count = count() | extend TableName = "ThreatIntelIndicators")
| where Count == 0
| project TableName, Count
```