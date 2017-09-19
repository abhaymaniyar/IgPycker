""" This is a python program to get Instagram Profile Photo of entered User.

	Usage:
	Method 1) Call the program direclty using following command:
				"python3 pycker.py"
			  and you will be prompted with the username.
	 
	Method 2) Import the package in python3 REPL(opened in the same directory as the program) using following command:
			"from pycker import *"
			  and execute the program using following command:
			  	"main()"
			  and you will be prompted with the username.

"""

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from PIL import Image
from bs4 import BeautifulSoup 

base_url = "https://www.instagram.com/"

""" Fetch an image from a url """
def fetch_image(user_name):
	try:
		profile = urlopen(base_url+user_name)
		profile_html = profile.read()
		soup = BeautifulSoup(profile_html, "lxml")
		images_tag = soup.find_all('img', {'class': '_9bt3u'})
		image_link = images_tag[0].attrs
		link_to_image = image_link.get('src')
		better_link = link_to_image[0:link_to_image.find('/s150')] + link_to_image[link_to_image.find('150/')+3:]
		image = urlopen(better_link)
		f = image.read()
		save_image(f)
	except HTTPError:
		print("ERROR: No user with this user name exist. Please enter correct username.")
	except URLError:
		print("ERROR: Couldn't connect to the server. Please check internet connection.")

""" Save a image with user entered file name"""
def save_image(jpg):
	try:
		name_of_file = input("Enter file name: ")
		f = open(name_of_file+'.jpg', 'wb')
		f.write(jpg)
		img = Image.open(name_of_file+'.jpg')
		img.show()
	except Exception:
		print("ERROR: Something Went Wrong! File couldn't be saved. Try Again and make sure your internet is turned on.")

def main():
	user_name = input("Enter User name: ")
	fetch_image(user_name)


if __name__ == "__main__":
	main()

