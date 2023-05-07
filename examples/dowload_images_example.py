from zack.core import Scraper
from zack.utils import download_images

url = "https://www.yeswehack.com/fr/entreprises/pourquoi-le-bug-bounty/"
url_base = "https://www.yeswehack.com/"
scraper = Scraper(url)
images = scraper.get_images_url()
output_directory = "images"

download_images(url_base, images, output_directory)