from bs4 import BeautifulSoup
import urllib.request
import re
import json

lists = []
langueges =[]
html = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_programming_languages")
soup = BeautifulSoup(html.read(),"lxml")
lists.extend(soup.find_all("div",{'class':'div-col columns column-width'}))
for section in lists:
    for elem in section.findAll("ul"):
        for link in elem.findAll("a"):
            langueges.append(link.text)


with open('languages.json', 'w') as outfile:
    json.dump(langueges, outfile)