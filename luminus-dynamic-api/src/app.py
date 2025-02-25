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
    level=logging.INFO,
)


@app.route("/healthz")
def health_check():
    return "OK", 200


@app.route("/", methods=["GET"])
def main():
    try:
        return get_data()
    except Exception as e:
        return Response({"error": e}, status=500)
