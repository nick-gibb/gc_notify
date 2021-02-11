import json
import requests
import config
import base64

api_key = config.api_key


def base64_encode(filename):
    file_contents = open(filename, "r").read()
    encoded_file_contents = base64.b64encode(bytes(file_contents, "utf-8")).decode("ascii")
    return encoded_file_contents


def send_email(email_address="nicholas.gibb@canada.ca", filename=None):
    url = "https://api.notification.canada.ca/v2/notifications/email"
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

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    print(r.text)


def main(files):
    for filename in files:
        # filename_base64 = base64_encode(filename)
        print(filename)
        send_email("nicholas.gibb@canada.ca", filename)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
