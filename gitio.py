import requests
import argparse
import sys

API_URL = "https://git.io/create"
HOME_URL = "https://git.io/"
ERROR = "Must be a GitHub.com URL."

def shorten(url, custom_code=None):
	data = requests.post(API_URL, data={"url":url}).text

	if data == ERROR:
		print(ERROR)
	else:
		print(HOME_URL+data)


def main():
	parser = argparse.ArgumentParser(description = "Create short GitHub url from the terminal")

	parser.add_argument("-u", "--url",
			type=str,
			required=True,
			help = "GitHub url")

	args = parser.parse_args()


	if len(sys.argv) == 1: # if argument is given then show help
		parser.print_help()

	elif args.url:
		shorten(args.url)


if __name__=="__main__":
	main()