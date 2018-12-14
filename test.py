# %%

from bs4 import BeautifulSoup
import urllib.request
from html5print import HTMLBeautifier
import tech
import html

i = 1
Page = []
techArray = []
for i in range(1, 2):
    htmlPage = urllib.request.urlopen(
        "https://stackoverflow.com/questions/tagged/javascript?sort=newest&page="+str(i)+"&pagesize=50")
    soup = BeautifulSoup(htmlPage.read(), "html.parser")
    Page.extend(soup.find_all("div", "summary"))
    tempQustionsArray = soup.find_all("div", "summary")
    z = 0
    for z in range(0, len(tempQustionsArray)):
        header = (tempQustionsArray[z].find("a", "question-hyperlink")).text
        print(header)

        href = (tempQustionsArray[z].find("a", "question-hyperlink")).get("href")
        print(href)

        relativeTime = (tempQustionsArray[z].find("span", "relativetime")).get("title")
        print(relativeTime)

        qustion = (tempQustionsArray[z].find("div", "excerpt")).text
        print(qustion)

        qId = href.rsplit('/', 2)[1]
        print(qId)

        tags = []
        tagesArraytempIndex = 0
        tagesArraytemp = (tempQustionsArray[z].find_all("a", "post-tag"))
        for tagesArraytempIndex in range(0, len(tagesArraytemp)):
            tags.append(tagesArraytemp[tagesArraytempIndex].text)
        print(tags)
        
        techArray.append(
            tech.Tech(header, qustion, tags, qId, relativeTime, href))

        print('-------------------------------------------------------------------')

#printing using override
for a in techArray:
    print(a)
