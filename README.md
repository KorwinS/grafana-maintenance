# Grafana Management Tools

A collection of scripts and random junk that we use to work with Grafana.

## Scripts

### alert_check.py

We found an odd bug where the alerting engine in Grafana crashed, but the app kept running and no one knew about it, while the alerts were stuck in a pending state. This python script runs as a cron job on the Grafana EC2 hosts, hits the Grafana API, and checks to see if more than half of the alerts are "pending", and sends a notification to SNS if it is.

### alert_shh.py

Starts a "Maintenance Mode" for Grafana when we need to take down InfluxDB. This script will generate a simple txt file with the IDs of the alerts

Requires a `configuration.py` (example below) file with prod and test info to be in the same directory as the script. The Bearer token is generated from the Grafana UI.

### alert_reviver.py

Takes Grafana out of "Maintenance Mode" by reading the values in the txt file in the directory.

---

Example `configuration.py`:

```python
#!/usr/bin/env python3

prod = {
    'host': 'grafana.qlmetrics.com',
    'token': 'Bearer {TOKEN HERE}'
}

test = {
    'host': 'test.squigglelines.com',
    'token': 'Bearer {TOKEN HERE}'
}
```
