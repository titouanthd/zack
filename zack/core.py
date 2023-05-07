import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        # print("Fetching page")
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to fetch page")

    def parse_page(self, html):
        # print("Parsing page")
        # Use BeautifulSoup or any other HTML parsing library to extract data from the HTML content
        # Example:
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_page(self):
        # print("Getting page")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup

    # Add more methods here if needed

    # Method to get only the body of the page
    def get_body(self):
        # print("Getting body")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup.body

    # Method to get only the title of the page
    def get_title(self):
        # print("Getting title")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup.title.text

    # Method to get only the head of the page
    def get_head(self):
        # print("Getting head")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup.head







