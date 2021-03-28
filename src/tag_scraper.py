from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#let's make a scraper
subject_page = 'https://www.brainpickings.org/all-subjects/'
#query the site and return the html and store it
page = urlopen(subject_page)
#parse the html and store it
soup = BeautifulSoup(page, 'html.parser')
tags = soup.find('h4', attrs={'class' : 'tags'})

tag_list = [list(tag.children)[0] for tag in list(tags.children)]

tag_dict = dict()
for tag in tag_list:
	k, v = tag.rsplit(maxsplit=1)
	tag_dict[k] = int(v.strip('()'))

pd.DataFrame.from_dict(data=tag_dict, orient='index').to_csv('brainpickings_tags.csv', header=False)
