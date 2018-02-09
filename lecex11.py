
#scrapebsoup.py

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

uhand = urllib.request.urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup")

html = uhand.read()
soup = BeautifulSoup(html, 'html.parser')

print(type(soup))

for h1 in soup.find_all('h1'):
    print(h1.get_text())

section_div = soup.find(id='searching-the-tree')
i = 0
for snippet in section_div.find_all(class_="highlight-python"):
    print("*** SNIPPET {} ***".format(i))
    print(snippet.get_text())
    i += 1
