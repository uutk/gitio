import requests
import argparse
import sys

API_URL = "https://git.io/create"
HOME_URL = "https://git.io/"

######### Errors #########
ERROR = "Must be a GitHub.com URL."
INVALID_URL = "Invalid url:"
##########################

def shorten(url):
	# Note to self: test the "code" data to add a custom code
	try:
		data = requests.post(API_URL, data={"url":url}).text
	except:
		print("Please check your internet conection.")
		exit()

	if data == ERROR:
		print(data)

	elif INVALID_URL in data:
		print(data)

	else:
		print(HOME_URL + data)


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
