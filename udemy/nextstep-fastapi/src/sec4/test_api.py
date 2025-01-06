import requests
import json

def main():
    url = "http://127.0.0.1:8000/item/"
    body = {
        "name": "t-shirts",
        "description": "long",
        "price": 1000,
        "tax": 1.1
    }
    res = requests.post(url, json.dumps(body)) #json形式（""")に変換
    print(res.json())

if __name__ == "__main__":
    main()