import argparse
from urllib.request import urlopen
import csv


def main(url):

    with urlopen(url) as csv_file:
        # csv_list = [i.decode("utf-8") for i in csv_file]

        # for line in csv_list:
        #     print(type(line), line)

        csv_reader = csv.reader(csv_file)
        



if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url) 