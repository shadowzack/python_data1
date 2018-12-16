#%%
### in VS code you can use juypter notebook by clicking on the symbols above (assuming that ypu have the extinsion)

from bs4 import BeautifulSoup
from json import JSONEncoder
import urllib.request
import tech
import html
import tech
import json
import sys

### getting all languges
with open('languages.json') as f:
    langes = json.load(f)
    
index = 1       ### page index
maxPage = 10    ### max number of pages for each languge
locker = 0      ### locker for checking if avaible pages number is smaller than maxPage
Page = []       ### Tech Object Array with all the results
techArray = []  ### Tech Object Array with all the results

### open Data 1 file all STDOUT data are printed to the file
sys.stdout = open("Data1.json", "a")


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
        if locker == 0:
            pagesNum = soup.find("div","pager fl").findAll("a")
            if(len(pagesNum)>2):
                maxPage = int(pagesNum[len(pagesNum)-2].find("span").text)
                locker=1


        ### questions crawler starts here 
        Page.extend(soup.find_all("div", "summary"))
       
        for section in Page:

            header = (section.find("a", "question-hyperlink")).text
       
            href = (section.find("a", "question-hyperlink")).get("href")
            try: 
                relativeTime = (section.find("span", "relativetime")).get("title")
            except:
                relativeTime = "no time"

            qustion = (section.find("div", "excerpt")).text
       
            qId = href.rsplit('/', 2)[1]

            tags = []
            tagesArraytempIndex = 0
            tagesArraytemp = (section.find_all("a", "post-tag"))
            for tagesArraytempIndex in tagesArraytemp:
                tags.append(tagesArraytempIndex.text)
            
            techObject=tech.Tech(header, qustion, tags, qId, relativeTime, href)
            techArray.append(techObject)

            json_string = json.dumps(techObject.__dict__)
            print(json_string)
          

sys.stdout.close()

#sys.stdout = open("Data1.json", "a")
#json_string = json.dumps([ob.__dict__ for ob in techArray])
#print(json_string)
