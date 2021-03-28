import requests

#All articles as of 3/28/2021
for page in range(1, 1426):
	url = f'http://www.brainpickings.org/page/{page}/'
	r = requests.get(url)

	with open(f'pages/{page}.txt', 'w') as file:
		file.write(r.text)