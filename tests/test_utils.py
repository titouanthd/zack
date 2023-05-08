import unittest
import os
from zack.core import Scraper
from zack.utils import clean_text, sanitize_filename, save_data_to_text_file, download_images

class TestUtils(unittest.TestCase):
    def test_clean_text(self):
        text = "<p>Hello, <em>world!</em></p>"
        cleaned_text = clean_text(text)
        self.assertEqual(cleaned_text, "Hello, world!")
        # Add more assertions as needed

    def test_sanitize_filename(self):
        filename = "Hello, world"
        sanitized_filename = sanitize_filename(filename)
        # assert matching pattern
        self.assertRegex(sanitized_filename, r'^hello_world_[a-z0-9]{4}$')

    def test_save_data_to_text_file(self):
        data = "Hello, world!"
        filename = "test_file"
        filename = save_data_to_text_file(data, filename, folder="tmp")
        self.assertTrue(os.path.exists("tmp/{}.txt".format(filename)))

        # remove the file
        os.remove("tmp/{}.txt".format(filename))


if __name__ == "__main__":
    unittest.main()