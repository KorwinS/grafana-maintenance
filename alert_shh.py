#!/usr/bin/env python3
import requests
import configuration as cfg
import os
from pathlib import Path
import time

URL = "https://" + cfg.test['host']
HEADERS = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Authorization': cfg.test['token']
}


def get_alerts():
    """
    Hit Grafana API and get alert state
    Returns active alert IDs
    """

    alerts = requests.get(url=URL + '/api/alerts',
                          verify=False,
                          headers=HEADERS).json()

    alerting = []
    i = 0
    while i < len(alerts):
        state = alerts[i]['state']
        if state != "paused":
            alerting.append(alerts[i]['id'])
        i = i + 1
    print(alerting)  # For manual testing
    return alerting


def save_ids(alert_id):
    """
    Write the IDs to a temporary csv
    Return the filename of the csv
    """

    save_path = os.getcwd()
    complete_name = os.path.join(save_path, "alert-ids.txt")

    if Path(complete_name).exists():
        # delete
        os.remove(complete_name)
        print("Removing existing txt file...")
        time.sleep(2)

    with open(complete_name, 'w') as resultFile:
        for x in alert_id:
            resultFile.write(str(x) + "\n")

    return complete_name


def silence(alert_id):
    """Pause the alerts based on the IDs passed into the function"""

    for x in alert_id:
        payload = "{\n  \"paused\": true\n}"

        response = requests.request("POST",
                                    URL + "/api/alerts/" + str(x) + "/pause",
                                    data=payload,
                                    verify=False,
                                    headers=HEADERS)
        print(response.text)


if __name__ == "__main__":
    alert_ids = get_alerts()
    save_ids(alert_ids)
    silence(alert_ids)
