import requests

import sys

url = "http://aigw-processors-f5:8000/api/v1/signature/f5/prompt-injection"

try:

    response = requests.get(url)

    if response.status_code == 200:

        print("Request successful: 200 OK")

    else:

        print(f"Request failed: {response.status_code}")

        sys.exit(1)

except requests.exceptions.RequestException as e:

    print(f"Request failed: {e}")

    sys.exit(1)