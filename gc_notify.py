import json
import requests
import config
import base64

api_key = config.api_key
email_list = config.emails
GC_NOTIFY_SERVICE = "https://api.notification.canada.ca/v2/notifications/email"


def base64_encode(filename):
    with open(filename, "rb") as file_contents:
        return base64.b64encode(file_contents.read()).decode("ascii")


def send_email(email_address, filename):
    encoded_file_contents = base64_encode(filename)

    payload = {
        "email_address": email_address,
        "template_id": "fb886753-58e7-4aac-bf08-c72b14de8fe6",
        "personalisation": {
            "first_name": "Nick",
            "link_to_file": {"file": encoded_file_contents},
        },
    }

    headers = {"content-type": "application/json", "Authorization": api_key}

    r = requests.post(GC_NOTIFY_SERVICE, data=json.dumps(payload), headers=headers)


def main(files):
    for filename in files:
        for email in email_list:
            send_email(email, filename)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
