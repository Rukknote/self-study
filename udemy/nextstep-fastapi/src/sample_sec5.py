import json

import requests


def main():
    url = "http://127.0.0.1:8000"
    data = {"x": 4.0, "y": 3.0}
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == "__main__":
    main()
