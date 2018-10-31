#!/usr/bin/env python3
import requests
import json
import configuration as cfg


def create_datasource(ds_name, dbname, influx_url, influx_user, influx_pass):
    """POST to Grafana's API and create Influxdb Datasource"""

    url = cfg.prod['url']
    token = cfg.prod['token']

    payload = {
        "name": ds_name,
        "type": "influxdb",
        "url": influx_url,
        "database": dbname,
        "access": "proxy",
        "user": influx_user,
        "password": influx_pass,
        "jsonData": {
            "keepCookies": {}
        }
    }

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': f"Bearer {token}",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST",
                                url,
                                data=json.dumps(payload),
                                headers=headers)

    print(response.text)  # Testing
    return response.text


if __name__ == "__main__":
    create_datasource(ds_name="ds_name",
                      dbname="dbname",
                      influx_url="influx_url",
                      influx_user="influx_user",
                      influx_pass="influx_pass")
