import argparse
from zack.core import Scraper


def setup_parser():
    parser = argparse.ArgumentParser(description="Zack Web Scraper CLI")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("-o", "--output", help="Output file path")
    return parser


def scrape_website(url, output):
    scraper = Scraper(url)
    data = scraper.get_page()

    # Process and utilize the scraped data as needed

    if output:
        # Save the data to the specified output file
        with open(output, "w") as f:
            # convert the data to a string
            data = str(data)
            f.write(data)
    else:
        # Output the data to the console
        print(data)


def main():
    parser = setup_parser()
    args = parser.parse_args()

    # Call the scrape_website function with the provided arguments
    scrape_website(args.url, args.output)


if __name__ == "__main__":
    main()
