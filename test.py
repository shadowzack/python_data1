#%%

from bs4 import BeautifulSoup
import urllib.request

i=1
Page=[]
for i in range(1,6):
    html = urllib.request.urlopen("https://stackoverflow.com/questions/tagged/javascript?sort=newest&page="+str(i)+"&pagesize=50")
    soup = BeautifulSoup(html.read(),"html.parser")
    Page.extend(soup.find_all("div","summary"))
    print(i)
print(len(Page))
