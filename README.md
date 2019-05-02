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

### datasource_name_updates.py

Updates the name of a datasource in all dashboard json in a directory. Useful if you decide to standardize on datasource names after the fact.

### cw_datasource.py

A script to create a Cloudwatch data source via the Grafana API. The `create_datasource()` function takes 4 arguments:

- ds_name: String - Name of the Data Source. Example "Lead Allocation Prod"
- account_num: String - AWS account number
- aws_region: String - Set the default AWS region for the data source.
- role_name: String - Name of the IAM role for account access. 

### influx_datasource.py

A script to create an Influxdb data source via the Grafana API. The `create_datasource()` function takes 5 arguments:

- ds_name: String - Name of the Data Source. Example "Lead Allocation Prod"
- dbname: String - Name of the InfluxDB database
- influx_url: String - Url of the InfluxDB API
- influx_user: String - User name for InfluxDB Credentials
- influx_pass: String - Password for InfluxDB Credentials

### user_emails.py

A script to gather a list of email addresses of users via the Grafana API. The `email_txt()` function takes 1 argument:

- email_list: List - List of all email addresses from the `get_users()` function.

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
