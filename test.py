# %%

from bs4 import BeautifulSoup
import urllib.request
from lxml import etree, html
from html5print import HTMLBeautifier
from html.parser import HTMLParser
import tech 

i = 1
Page = []
for i in range(1, 2):
    htmlPage = urllib.request.urlopen(
        "https://stackoverflow.com/questions/tagged/javascript?sort=newest&page="+str(i)+"&pagesize=50")
    soup = BeautifulSoup(htmlPage.read(), "html.parser")
    Page.extend(soup.find_all("div", "summary"))
   # print(i)

print(Page[0])
temp=tech.Tech(1,1,1,1,1)
print(str(temp))