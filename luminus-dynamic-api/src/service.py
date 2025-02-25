import json
from typing import List, Any, Dict

import requests
from bs4 import BeautifulSoup

from cache import session
from models import *


def get_data() -> List[Dict[str, Any]]:
    url = "https://my.luminusbusiness.be/market-info/nl/dynamic-prices/"

    try:
        headers = {}
        resp = session.get(
            url, headers=headers, stream=True, timeout=10, allow_redirects=True
        )

        if resp.status_code != 200:
            return [{"error": resp.json()}]

        soup = BeautifulSoup(resp.content, "html.parser")
        data = soup.find("script", {"id": "__NEXT_DATA__"}).contents

        return format_data(json.loads(str(data[0])))

    except requests.exceptions.RequestException as e:
        raise e


def process_price_data(price_data, date) -> List[Dict[str, Any]]:
    date_format = "%Y-%m-%d %H:%M:%S"
    prices = []
    for row in price_data:
        price = EnergyPrice(
            date=datetime.strptime(row["datetime"], date_format).replace(year=date.year, month=date.month, day=date.day),
            price=float(row["value"])
        )
        prices.append(price.to_json())

    return prices


def format_data(data):
    date_format_other = "%Y-%m-%d"

    today = datetime.strptime(data["props"]["pageProps"]['today'][:10], date_format_other)
    tomorrow = datetime.strptime(data["props"]["pageProps"]['tomorrow'][:10], date_format_other)

    # Process today's price data
    new_data = process_price_data(data["props"]["pageProps"]["todaysAndTomorrowsPriceData"]["todaysPriceData"], today)

    # Process tomorrow's price data
    new_data = new_data + process_price_data(
        data["props"]["pageProps"]["todaysAndTomorrowsPriceData"]["tomorrowsPriceData"], tomorrow)

    return new_data
