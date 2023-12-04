"""
usage: python3 local-chaos-scraper.py

Fetches scans of zines from every page listed at https://localchaos.org/zine_listing.html
"""

import PIL
from PIL import Image, UnidentifiedImageError
from bs4 import BeautifulSoup
import os
import requests

#use these to get live page
#r = requests.get('https://localchaos.org/zine_listing.html')
#with open(r) as fp:

with open('/home/nadia/Downloads/zines.html') as fp:
	main_soup = BeautifulSoup(fp, 'html.parser')

links = main_soup.find_all("a")
for link in links:
	print('link', link)
	url = link['href']
	page_r = requests.get(url)
	page_soup = BeautifulSoup(page_r.text, 'html.parser')
	pagedir = "/home/nadia/Downloads/" + url.split('/')[3][:-5]
	print('pagedir', pagedir)
	if not os.path.exists(pagedir):
		os.makedirs(pagedir)
	for img_html in page_soup.find_all("img")[:-1]:
		image_url = "https://localchaos.org/" + img_html['src']
		print('img src', image_url)
		try:
			image = Image.open(requests.get(image_url, stream = True).raw)
		except PIL.UnidentifiedImageError:
			print('image error:', image_url)
		filename = image_url.split('/')[-1]
		image.save(pagedir + "/" + filename)
