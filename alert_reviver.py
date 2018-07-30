#!/usr/bin/env python3
import requests
import configuration as cfg
from pathlib import Path
import os


URL = "https://" + cfg.test['host']
HEADERS = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Authorization': cfg.test['token']
}


def get_filename():
    """
    Check if CSV is in the working directory
    Returns full path and filename
    """

    current = os.getcwd()
    complete_name = os.path.join(current, "alert-ids.txt")

    # Check if the file exists
    try:
        Path(complete_name).exists()
        valid_file = complete_name
    except:
        print("No alert-ids.txt file found")

    return valid_file


def resurrect(filepath):
    """Restart the alerts based on the IDs in the txt file"""

    # Get list from csv
    with open(filepath, 'r') as txt:
        data = txt.readlines()

    alert_ids = []

    for line in data:
        alert_ids.append(int(line))

    print(alert_ids)
    for x in alert_ids:
        payload = "{\n  \"paused\": false\n}"

        response = requests.request("POST",
                                    URL + "/api/alerts/" + str(x) + "/pause",
                                    data=payload,
                                    verify=False,
                                    headers=HEADERS)
        print(response.text)

if __name__ == "__main__":
    file = get_filename()
    resurrect(file)
