import requests
from bs4 import BeautifulSoup
import pandas as pd


def scraper(page_count):
    """
	Saves html source for all articles as txt files
	Args: int
	"""
    for page in range(1, page_count+1):
        url = f'http://www.brainpickings.org/page/{page}/'
        r = requests.get(url)

        with open(f'data/pages/0.txt', 'w') as file:
            file.write(r.text)

            
def parse_html(data, soup, ix):
	"""
	Takes soup and returns the fields of the articles.
	Args: int
	Returns: list
	"""
	i=0  # these two variables create an index
	j=len(soup.find_all("h1", {"class": "entry-title"}))
	
    # find where the articles start within html
	for h in soup.find_all("h1", {"class": "entry-title"}):
        # reversed index
		index = ix+j-i
		title = str(h.text + " - " + h.find_next_sibling().get_text())
		url = h.a.get('href')
        #the data is cleverly hidden in the url
		date = str(h.a)[39:49]
        
        #this part extracts tags
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
        
        #and this part finally gets to the content of the article
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
        
        # a word counter counting any space-divided string with a letter in it
		title_len = sum(1 for word in title.split() if any(c.isalpha() for c in word))
		content_len = sum(1 for word in content.split() if any(c.isalpha() for c in word))
		words = title_len + content_len
		# data is a big list of dictionaries for every article
		data.append(dict(index=index, title=title, url=url, date=date,
							tags=tags, words=words, content=content))

	return i, data


def article_df(page_count):
	"""
	Loads files individually then passes them to parse function.
    Saves final list as csv.
	Args: int
	"""
	ix=0
	data=[]
	for page in range (page_count-1, -1, -1):
		file = open(f'data/pages/{page}.txt')
		soup = BeautifulSoup(file.read(), "html.parser")
		i, data = parse_html(data, soup, ix)
		ix+=i
	df = pd.DataFrame(data)
	df = df.sort_values("index")
	df.to_csv('data/articles.csv', index=False)


if __name__ == "__main__":
	#1426 pages on brainpickings.org as of 4/4/2021
	page_count = 1426
	#next line took about a half-hour
	#scraper(page_count)
	article_df(page_count)
