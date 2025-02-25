#!/usr/bin/env python

from app import main, logging
if __name__ == "__main__":
    logging.info("Starting sync")
    main()
    logging.info("Sync done")
