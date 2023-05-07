import time

from zack.core import Scraper
from zack.utils import Logger

# Create a Scraper instance
url = "https://google.com"
scraper = Scraper(url)

# Create a Logger instance
logger = Logger()

# Perform scraping
started_at = time.time()
print("Get title ?")
title = scraper.get_title()

# Log a message after scraping
ended_at = time.time()
logger.log("Scraping process completed in {} seconds".format(ended_at - started_at))

# Display the scraped data
print("Title:", title)