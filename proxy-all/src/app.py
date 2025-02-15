#!/usr/bin/env python

from flask import Flask, request, Response
import requests
import urllib.parse
import logging
from bs4 import BeautifulSoup
from pygments.lexers import guess_lexer

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

ALLOWED_DOMAINS = []


def prepend_base_url(base_url: str, target_base_url: str, url: str) -> str:
    if url.startswith(("http://", "https://")):
        return base_url + "?q=" + urllib.parse.quote_plus(url)
    else:
        return (
            base_url
            + "?q="
            + urllib.parse.quote_plus(target_base_url + url.lstrip("/"))
        )


@app.route("/", methods=["GET"])
def proxy():
    target_url = request.args.get("q")
    if not target_url:
        return Response("Missing 'q' query parameter.", status=400)

    try:
        headers = {key: value for key, value in request.headers if key != "Host"}
        headers = {}
        resp = requests.get(
            target_url, headers=headers, stream=True, timeout=10, allow_redirects=True
        )

        if resp.status_code != 200:
            return resp

        excluded_headers = [
            "content-encoding",
            "transfer-encoding",
            "connection",
            "x-frame-options",
        ]
        headers = [
            (name, value)
            for (name, value) in resp.raw.headers.items()
            if name.lower() not in excluded_headers
        ]

        logging.info(f"Proxied URL: {target_url} | Status: {resp.status_code}")

        soup = BeautifulSoup(resp.content, "html.parser")
        language = guess_lexer(resp.content).name

        base_url = request.base_url.replace("http://", "//")
        content = resp.content
        if bool(soup.find()) and language in ["XML", "HTML"]:
            for tag in soup.find_all(href=True):
                tag["href"] = prepend_base_url(base_url, target_url, tag["href"])

            for tag in soup.find_all(src=True):
                tag["src"] = prepend_base_url(base_url, target_url, tag["src"])

            content = soup.encode("utf8")

        return Response(content, resp.status_code, headers)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {target_url}: {e}")
        return Response(f"Error fetching the URL: {e}", status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
