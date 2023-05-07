from zack.core import Scraper
from zack.utils import save_data_to_text_file

# Create a Scraper instance
url = "https://google.com"
scraper = Scraper(url)

# Perform scraping
data = scraper.get_title()

# Save the scraped data to a file 
filename = "scraped_data"
folder_absolute_path = "C:/Users/%username%/Desktop" # replace by your own path
filename = save_data_to_text_file(data, filename, folder=folder_absolute_path)

print("Data saved to", filename)