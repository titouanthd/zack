import re
import uuid
import os

def clean_text(text):
    # Clean up the text by removing unwanted characters and extra spaces
    clean_text = re.sub(r'\s+', ' ', text)
    clean_text = re.sub('<.*?>', '', clean_text)
    return clean_text

def save_data_to_text_file(data, filename, folder="files") -> str:
    # check if folder exists if not return error
    if not os.path.exists(folder):
        raise Exception("Folder does not exist")


    filename = sanitize_filename(filename)
    # Save the data to a text file
    with open("{}/{}.txt".format(folder, filename), 'w') as file:
        file.write(data)

    return filename

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

class Logger:
    def __init__(self, log_file='logs/messages.log'):
        self.log_file = log_file

    def log(self, message):
        # Log messages to a log file for tracking and debugging purposes
        # Example:
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')