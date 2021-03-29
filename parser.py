import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_articles(data, soup, ix):
	"""
	Takes soup and returns the fields of the articles.
	Args: int
	Returns: list
	"""
	i=0
	j=len(soup.find_all("h1", {"class": "entry-title"}))
	
	for h in soup.find_all("h1", {"class": "entry-title"}):
		index = ix+j-i
		title = str(h.text + " - " + h.find_next_sibling().get_text())
		url = h.a.get('href')
		date = str(h.a)[39:49]

		tag = soup.find_all(id="posts")[i]
		tag_set = list()
		for child in tag.get('class'):
			if child[:3] == "tag":
				tag_set.append(child[4:])
			elif child[:8] == "category":
				tag_set.append(child[9:])
		tag_set = set(tag_set)
		tags = str()
		for tag in tag_set:
			tags += tag + ", "

		i+=1

		html = u""
		for tag in h.next_siblings:
			if str(tag)[:3] in ["<h2","<h3"]: continue
			if tag == "!--END posts--": break
			text = str(tag).replace("\n","")
			html += text

		html_soup = BeautifulSoup(html, "html.parser")
		text = html_soup.findAll(text=True)
		content = str()
		for t in text:
			content += t + " "

		words = len(title.split()) + len(content.split())
		
		data.append(dict(index=index, title=title, url=url, date=date,
							tags=tags, words=words, content=content))

	return i, data


def article_loader(page_count):
	"""
	Loads files individually. Saves final list as csv.
	Args: int
	"""
	ix=0
	data=[]
	for page in range (page_count, 0, -1):
		file = open(f'data/{page}.txt')
		soup = BeautifulSoup(file.read(), "html.parser")
		i, data = extract_articles(data, soup, ix)
		ix+=i
	df = pd.DataFrame(data)
	df.to_csv('data/articles.csv', index=False)


if __name__ == "__main__":

	#1425 pages scraped from brainpickings.org
	page_count = 1425
	article_loader(page_count)