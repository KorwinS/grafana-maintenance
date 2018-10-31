import requests
import boto3
import sys
import configuration as cfg


# Prep the sns stuff
client = boto3.client('sns', region_name='us-east-1')


HEADERS = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Authorization': cfg.prod['token']
}
SNSARN = cfg.prod['snsarn']


def alert_checker():
    """
    Checks for alert state using Grafana API
    """

    alerts = requests.get(url='http://localhost:3000/api/alerts',
                          headers=HEADERS).json()
    pending = requests.get(
        url='http://localhost:3000/api/alerts?state=pending',
        headers=HEADERS).json()
    percent_pending = float(len(pending)) / float(len(alerts))
    # print percent_pending # testing
    if percent_pending >= 0.5:
        # Send your sms message.
        client.publish(
            TopicArn=SNSARN,
            Message="Check Grafana Alerts!"
        )
        state = 'Alerts need attention'
    else:
        state = 'ok'
    return state


if __name__ == "__main__":
    alert_checker()
