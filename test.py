# %%

from bs4 import BeautifulSoup
import urllib.request
# from html5print import HTMLBeautifier
import tech
import html
from json import JSONEncoder
import tech
import json
import sys

with open('languages.json') as f:
    langes = json.load(f)
    
i = 1 
maxPage = 10
locker = 0 
Page = []
techArray = []
for lang in langes:
    locker = 0
    for i in range(1, maxPage):
        try:
            htmlPage = urllib.request.urlopen(
                "https://stackoverflow.com/questions/tagged/"+lang+"?sort=newest&page="+str(i)+"&pagesize=50")
        except:
            break
        soup = BeautifulSoup(htmlPage.read(), "html.parser")

        ### getting Max page number
        ### one time each string
        if locker == 0 :
            pagesNum = soup.find("div","pager fl").findAll("a")
            maxPage = int(pagesNum[4].find("span").text)
            locker=1

        ### questions crawler starts here 
        Page.extend(soup.find_all("div", "summary"))
        # tempQustionsArray = soup.find_all("div", "summary")
        z = 0
        for section in Page:
            header = (section.find("a", "question-hyperlink")).text
            print(header)

            href = (section.find("a", "question-hyperlink")).get("href")
            print(href)

            relativeTime = (section.find("span", "relativetime")).get("title")
            print(relativeTime)

            qustion = (section.find("div", "excerpt")).text
            print(qustion)

            qId = href.rsplit('/', 2)[1]
            print(qId)

            tags = []
            tagesArraytempIndex = 0
            tagesArraytemp = (section.find_all("a", "post-tag"))
            for tagesArraytempIndex in tagesArraytemp:
                tags.append(tagesArraytempIndex.text)
            print(tags)
            
            techArray.append(
                tech.Tech(header, qustion, tags, qId, relativeTime, href))

            print('-------------------------------------------------------------------')






#sys.stdout = open("Data1.json", "w+")
#for a in techArray:
   # print(a)
   # json.dumps(a)
   #print(json.dumps(foo.__dict__))


# with open('languages.json', 'w') as outfile:
#     json.dump(langueges, outfile)


    #opens file for stdout all prints are printed to the file



    sys.stdout = open("Data1.json", "a")
    json_string = json.dumps([ob.__dict__ for ob in techArray])
    print(json_string)
    sys.stdout.close()


