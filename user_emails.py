#!/usr/bin/env python3
import requests
import configuration as cfg
from pathlib import Path
import os


host = cfg.prod['host']


URL = f"https://{host}"
HEADERS = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Authorization': cfg.admin_basic['basicAuth']
}


def get_users():
    """
    Hit Grafana API and get user emails
    Returns user's emails
    """

    users = requests.request("GET",
                             url=URL + '/api/users',
                             # verify=False,
                             headers=HEADERS).json()

    emails = []
    i = 0
    while i < len(users):
        emails.append(users[i]['email'])
        i = i + 1
    # print(emails)  # For manual testing
    return emails


def email_txt(email_list):
    """
    Write the list of IDs to a txt file
    Return the filename of the txt file
    """

    save_path = os.getcwd()
    complete_name = os.path.join(save_path, "user-emails.txt")

    if Path(complete_name).exists():
        # delete
        os.remove(complete_name)
        print("Removing existing txt file...")

    with open(complete_name, 'w') as resultFile:
        for x in email_list:
            resultFile.write(str(x) + "\n")

    print("User emails are in " + complete_name)
    return complete_name

if __name__ == "__main__":
    print("Getting users...")
    users = get_users()
    email_txt(users)
