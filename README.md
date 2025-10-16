# Grafana Backup & Monitoring
Automated backups with restore workflow and Teams notification.

## Flow
```mermaid
flowchart LR
  Sched[Cron/Action] --> Backup[Export dashboards & datasources]
  Backup --> Store[Blob/S3]
  Backup --> Notify[Teams Adaptive Card]
```

## Restore
```bash
grafana-backup restore --from ./artifacts/latest.tgz --url $GRAFANA_URL --token $TOKEN
```

## Outcome
- Backups verified; restore < 2 min for typical set
