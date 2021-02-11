import json
import requests
import config

api_key = config.api_key


def send_email(email_address="nicholas.gibb@canada.ca"):
    url = "https://api.notification.canada.ca/v2/notifications/email"
    payload = {
        "email_address": email_address,
        "template_id": "fb886753-58e7-4aac-bf08-c72b14de8fe6",
        "personalisation": {
            "first_name": "Nick",
            #    "link_to_file": {
            #        "file": "test.txt"
            #    }
        },
    }

    headers = {"content-type": "application/json", "Authorization": api_key}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    # print(r.text)


def main(args):
    print(args)
    send_email()


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
