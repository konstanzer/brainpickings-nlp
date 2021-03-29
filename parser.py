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
		date = str(h.a)[39:49]

		tag = soup.find_all(id="posts")[i]
		tags = list()
		for child in tag.get('class'):
			if child[:3] == "tag":
				tags.append(child[4:])
		i+=1

		html = u""
		for tag in h.next_siblings:
			if str(tag)[:3] in ["<h2","<h3"]: continue
			if tag == "!--END posts--": break
			content = str(tag).replace("\n","")
			html += content
		html_soup = BeautifulSoup(html, "html.parser")
		content = html_soup.findAll(text=True)

		data.append(dict(index=index, title=title, date=date, tags=tags, content=content))

	return i, data


def article_loader(page_count):
	"""
	Loads files individually.
	Args: int
	"""
	ix=0
	data=[]
	for page in range (page_count, 0, -1):
		file = open(f'pages/{page}.txt')
		soup = BeautifulSoup(file.read(), "html.parser")
		i, data = extract_articles(data, soup, ix)
		ix+=i
	df = pd.DataFrame(data)
	df.to_csv('pages/articles.csv', index=False)


if __name__ == "__main__":

	#1425 pages scraped from brainpickings.org
	page_count = 1425
	article_loader(page_count)