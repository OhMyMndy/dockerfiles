#!/usr/bin/env python

from app import save_data, logging
from service import get_data

if __name__ == "__main__":
    logging.info("Starting sync")
    save_data(get_data())
    logging.info("Sync done")
