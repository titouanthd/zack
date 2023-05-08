# Zack - Python Web Scraper

Zack is a Python package for web scraping. It provides a simple and intuitive way to extract data from web pages.

## Installation

Clone the repository to your local machine:

```
git clone git@github.com:titouanthd/zack.git
```

Use pip to install the package:

```
pip install .
```

## Usage
To use the Zack package, follow these steps:

Import the Scraper class from zack.core:

```
from zack.core import Scraper
```

Create a Scraper instance with the URL you want to scrape:

```
url = "https://example.com"
scraper = Scraper(url)
```

Use the method to perform the scraping:

```
data = scraper.get_page()
```

The data variable will contain the scraped information.

Process and utilize the scraped data as needed.

## Examples
Here's an example of scraping a webpage using the Zack package:

```
from zack.core import Scraper

url = "https://example.com"
scraper = Scraper(url)
data = scraper.get_page()

# Process and utilize the scraped data
# ...

print(data)
```

For more examples, please refer to the examples directory.

## CLI Usage
The "zack" web scraper package includes a Command-Line Interface (CLI) that allows you to easily scrape websites and retrieve data from the command line. Follow the instructions below to utilize the CLI.

Prerequisites
Make sure you have Python 3 installed on your system. Additionally, install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

### Usage
To use the CLI, open your terminal or command prompt and navigate to the project directory. Then, you can run the cli.py script with the desired command-line arguments and options.

The general syntax for running the CLI is as follows:

```
python cli.py <url> [-o OUTPUT]
```

Replace <url> with the URL of the website you want to scrape. Optionally, you can provide the -o or --output option followed by the output file path to save the scraped data to a file instead of printing it to the console.

Here's an example of how to use the CLI:

```
python cli.py https://example.com -o output.txt
```

This command will scrape the specified URL (https://example.com) and save the scraped data to the file output.txt.

If no output file is specified, the scraped data will be printed to the console.

### Example
Here's an example of running the CLI without specifying an output file:

```
python cli.py https://example.com
```

This command will scrape https://example.com and print the scraped data to the console.

### Help
To display the available options and get more information about the CLI, you can use the --help option:

```
python cli.py --help
```

## Testing
The Zack package includes a set of tests to ensure its functionality. To run the tests, use the following command:

```
python -m unittest discover tests
```

## Contributing
Contributions are welcome! If you want to contribute to the Zack package, please follow these guidelines:

Fork the repository and clone it to your local machine.
Create a new branch for your feature or bug fix.
Make your modifications and write tests to ensure code coverage.
Run the existing tests to ensure they pass.
Commit your changes and push them to your fork.
Open a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.