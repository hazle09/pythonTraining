from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
keyword='한국어'
url='https://ko.wikipedia.org/wiki/'+parse.quote(keyword)
source=BeautifulSoup(urlopen(url),'html.parser')
target=source.find_all('li',{'class':'toclevel-1'})
body=source.find('div',{'id':'bodyContent'})
paragraphs=body.find_all('p')
웨
for p in paragraphs:
    print(p.get_text().strip())
    break