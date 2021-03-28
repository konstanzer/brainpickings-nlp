import requests
from bs4 import BeautifulSoup

#text = soup.findAll(text=True)
#headers  = ['style', 'script', '[document]', 'head', 'title']
#filtered = filter(lambda e: False if e.parent.name in headers else True, text)
#for s in filtered: print(s)

#print(soup.prettify())

#for link in soup.find_all('a'): print(link.get('href'))

#print(soup.get_text())
    
if __name__ == "__main__":
	#All articles as of 3/28/2021
	for page in range(1, 5):
		file = open(f'pages/{page}.txt')
		text = file.read()
		soup = BeautifulSoup(text)
		print(soup.get_text())