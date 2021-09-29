import argparse
from urllib.request import urlopen


def main(url):

    with urlopen(url) as x:
        print(x.read().decode("utf-8"))




if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url) 