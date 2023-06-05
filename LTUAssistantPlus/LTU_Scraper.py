import requests
from bs4 import BeautifulSoup

url = "https://www.ltu.edu/arts_sciences/mathematics_computer_science/"
content = requests.get(url, timeout = 5)

soup = BeautifulSoup(content.content, "html.parser")
#x = soup.find("a" , {"class":"article-link"}) 
t = soup.findAll("a", {"class":"article-link"})

for x in t:
	#y = t.find("a" , {"class":"article-link"})
	y = x.find(text = True)
	if y == None:
		pass
	else:
		print(y)