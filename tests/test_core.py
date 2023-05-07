import unittest
from zack.core import Scraper

class TestCore(unittest.TestCase):
    def test_fetch_page(self):
        url = "https://google.com"
        scraper = Scraper(url)
        data = scraper.fetch_page()
        self.assertIsNotNone(data)
        # Add more assertions as needed

    def test_parse_page(self):
        url = "https://google.com"
        scraper = Scraper(url)
        data = scraper.parse_page(scraper.fetch_page())
        self.assertIsNotNone(data)
        # Add more assertions as needed

    def test_get_page(self):
        url = "https://google.com"
        scraper = Scraper(url)
        data = scraper.get_page()
        self.assertIsNotNone(data)
        # Add more assertions as needed

    def test_get_title(self):
        url = "https://google.com"
        scraper = Scraper(url)
        data = scraper.get_title()
        self.assertIsNotNone(data)
        # Add more assertions as needed

    def test_get_body(self):
        url = "https://google.com"
        scraper = Scraper(url)
        data = scraper.get_body()
        self.assertIsNotNone(data)

    def test_get_head(self):
        url = "https://google.com"
        scraper = Scraper(url)
        data = scraper.get_head()
        self.assertIsNotNone(data)

    def test_get_meta_description(self):
        url = "https://siclem.fr"
        scraper = Scraper(url)
        data = scraper.get_meta_description()
        self.assertIsNotNone(data)

    # Add more tests as needed


if __name__ == "__main__":
    unittest.main()