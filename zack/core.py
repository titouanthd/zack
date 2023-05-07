import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    # Method to fetch the page
    def fetch_page(self):
        # print("Fetching page")
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to fetch page from {}".format(self.url + " " + str(response.status_code)))

    # Method to parse the page
    def parse_page(self, html):
        # print("Parsing page")
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    # Method to get the whole page
    def get_page(self):
        # print("Getting page")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup

    # Method to get only the head of the page
    def get_head(self):
        # print("Getting head")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup.head

    # Method to get only the body of the page
    def get_body(self):
        # print("Getting body")
        html = self.fetch_page()
        soup = self.parse_page(html)
        return soup.body

    # Method to get only the title of the page
    def get_title(self)->str:
        # print("Getting meta title")
        html = self.fetch_page()
        soup = self.parse_page(html)

        # check if title tag exists
        if soup.title is None:
            return ""

        return soup.title.text

    # Method to get only the meta description of the page
    def get_meta_description(self)->str:
        # print("Getting meta description")
        html = self.fetch_page()
        soup = self.parse_page(html)

        # check if meta description tag exists
        if soup.find('meta', attrs={'name': 'description'}) is None:
            return ""

        return soup.find('meta', attrs={'name': 'description'}).get('content')

    # Method to get the images of the page (empty list if no images)
    def get_images_url(self)->list:
        # print("Getting images")
        html = self.fetch_page()
        soup = self.parse_page(html)
        images = soup.find_all('img')
        src_attributes = [image.get('src') for image in images]
        return src_attributes

    # method to get elements by class
    def get_elements_by_class(self, class_name)->list:
        # print("Getting elements by class")
        html = self.fetch_page()
        soup = self.parse_page(html)
        elements = soup.find_all(class_=class_name)
        return elements

    # method to get elements by id
    def get_element_by_id(self, id_name)->list:
        # print("Getting elements by id")
        html = self.fetch_page()
        soup = self.parse_page(html)
        element = soup.find(id=id_name)
        return element

    # method to get elements by tag
    def get_elements_by_tag(self, tag_name)->list:
        # print("Getting elements by tag")
        html = self.fetch_page()
        soup = self.parse_page(html)
        elements = soup.find_all(tag_name)
        return elements

    # method to get a single element
    def get_element(self, selector):
        # print("Getting element")
        html = self.fetch_page()
        soup = self.parse_page(html)
        element = soup.select_one(selector)
        return element

    # method to get a list of elements
    def get_elements(self, selector):
        # print("Getting elements")
        html = self.fetch_page()
        soup = self.parse_page(html)
        elements = soup.find_all(selector)
        return elements
    
    # Add more methods here if needed







