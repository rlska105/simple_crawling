import requests
from bs4 import BeautifulSoup

req = requests.get("https://ginamkim.blogspot.com/")
html = req.text
soup = BeautifulSoup(html, "html.parser")

thetitles = soup.select('h3 > a')

#print(thetitles)

for title in thetitles:
    print(title.text)







