import re
import uuid
import os
import requests

def clean_text(text):
    # Clean up the text by removing unwanted characters and extra spaces
    clean_text = re.sub(r'\s+', ' ', text)
    clean_text = re.sub('<.*?>', '', clean_text)
    return clean_text

def sanitize_filename(filename):
    # Remove unwanted characters from the filename
    # unwanted characters include \ / * ? : " < > | , ; ' # & + = [ ] { }
    filename = re.sub(r'[\\/*?:"<>|,;\'#&+=\[\]{}]', '', filename)
    # Replace spaces with underscores
    filename = re.sub(r'\s+', '_', filename)
    # Remove extension if any
    filename = re.sub(r'\..*$', '', filename)
    # to lower case
    filename = filename.lower()
    # add uuid suffix to avoid overwriting existing files
    unique_suffix = str(uuid.uuid4())[:4]
    filename = "{}_{}".format(filename, unique_suffix)
    return filename

def url_is_valid(url: str)->bool:
    # check is not empty
    if url == "":
        return False
    # check if url contains a space
    if ' ' in url:
        return False
    return True

def save_data_to_text_file(data, filename, folder="datas/files") -> str:
    # check if folder exists if not return error
    if not os.path.exists(folder):
        # create the folder
        os.makedirs(folder)

    filename = sanitize_filename(filename)
    # Save the data to a text file
    with open("{}/{}.txt".format(folder, filename), 'w') as file:
        file.write(data)

    return filename

def download_images(url_base, image_urls, output_directory="data/images"):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for url in image_urls:
        # validate the url
        if not url_is_valid(url):
            print(f"Invalid url: {url}")
            continue

        # check if url starts with http or https
        if not url.startswith('http'):
            url = "{}{}".format(url_base, url)

        response = requests.get(url)

        if response.status_code == 200:
            filename = url.split('/')[-1]
            filepath = os.path.join(output_directory, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Image downloaded: {filename}")
        else:
            print(f"Failed to download image from {url}")

class Logger:
    def __init__(self, log_file='logs/messages.log'):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')