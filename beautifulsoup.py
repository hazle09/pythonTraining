# 기상청에서 날씨 알아보기
from urllib import request
from bs4 import BeautifulSoup

content=request.urlopen("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1153080000")
soup= BeautifulSoup(content, 'html.parser')

for data in soup.select("data"):
    print(data.select_one("wfKor").string)
    # .sting 이거 짱이다 ㅋㅋㅋㅋ 기호없이 글만 보여줌!
    print("-"*20)