#!/usr/bin/env python3
import requests
import json
import configuration as cfg


def create_datasource(ds_name, account_num, aws_region, role_name):
    """POST to Grafana's API and create Cloudwatch Datasource"""

    url = cfg.prod['url']
    token = cfg.prod['token']

    payload = {
        "name": ds_name,
        "type": "cloudwatch",
        "access": "proxy",
        "jsonData": {
            "authType": "arn",
            "defaultRegion": aws_region,
            "assumeRoleArn": f"arn:aws:iam::{account_num}:role/{role_name}"
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
    create_datasource(ds_name="name",
                      account_num="account_num",
                      aws_region="aws_region",
                      role_name="role_name")
