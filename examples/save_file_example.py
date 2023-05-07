from zack.core import Scraper
from zack.utils import save_data_to_text_file

# Create a Scraper instance
url = "https://siclem.fr"
scraper = Scraper(url)

# Perform scraping
data = scraper.get_meta_description()

# Save data to text file
save_data_to_text_file(data, "meta_description_siclem.txt")
