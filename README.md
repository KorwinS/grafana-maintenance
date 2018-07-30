# Grafana Maintenance Mode

Python scripts to pause and unpause active alerts via Grafana's Alerting API 

## Scripts

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
    'host': 'prod.hostname.com',
    'token': 'Bearer {TOKEN HERE}'
}

test = {
    'host': 'test.hostname.com',
    'token': 'Bearer {TOKEN HERE}'
}
```
