#!/usr/bin/env python
import logging
import os

from flask import Flask, Response

from models import *
from service import get_data

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///project.db")
db.init_app(app)

with app.app_context():
    db.create_all()

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", logging.INFO),
)


def save_data(energy_prices):
    logging.info("Saving data")
    date_format = "%Y-%m-%d %H:%M:%S"

    with app.app_context():
        for energy_price in energy_prices:
            found = (db.session.execute(db.select(EnergyPrice).filter_by(date = energy_price.date)).scalar_one_or_none())
            if found is None:
                logging.info(f"Inserting new energy price for date {energy_price.date.strftime(date_format)}, price {energy_price.price}")
                db.session.add(energy_price)

        db.session.commit()

@app.route("/healthz")
def health_check():
    return "OK", 200


@app.route("/", methods=["GET"])
def main():
    try:
        data = get_data()
        return data
    except Exception as e:
        return Response({"error": e}, status=500)
