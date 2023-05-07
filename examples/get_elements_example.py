from zack.core import Scraper

url = "https://www.yeswehack.com/fr/entreprises/pourquoi-le-bug-bounty/"
scraper = Scraper(url)

# get a single element
main = scraper.get_element_by_id("main")

print("Main:", main)

title = scraper.get_elements_by_class("title")

print("Title:", title)

h1 = scraper.get_elements_by_tag("h1")

print("H1:", h1)

# get a list of elements
images = scraper.get_elements("img")

print("Images:", images)

# get a single element
meta = scraper.get_element("main")

print("Meta:", meta)



