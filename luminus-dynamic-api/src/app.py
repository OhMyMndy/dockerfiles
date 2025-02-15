#!/usr/bin/env python

from typing import List
from flask import Flask, Response
import requests
import logging
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route("/healthz")
def health_check():
    return "OK", 200


@app.route("/", methods=["GET"])
def proxy():
    url = "https://my.luminusbusiness.be/market-info/nl/dynamic-prices/"

    try:
        headers = {}
        resp = requests.get(
            url, headers=headers, stream=True, timeout=10, allow_redirects=True
        )

        if resp.status_code != 200:
            return resp

        soup = BeautifulSoup(resp.content, "html.parser")
        data = soup.find("script", {"id": "__NEXT_DATA__"}).contents
        return json.loads(data[0])
    except requests.exceptions.RequestException as e:
        return Response({"error": e}, status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
