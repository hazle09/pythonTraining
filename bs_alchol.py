# from urllib import request
# from urllib.request import urlopen
# from urllib import parse
# from bs4 import BeautifulSoup

# url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

# source= BeautifulSoup(urlopen(url), 'html.parser')

# target=source.find_all({'drinks'},[{'strDrink'}])

# print(target)

# # for data in soup.select("drinks"):
# #     print(data.select_one("strDrink").string)
# #     # .sting 이거 짱이다 ㅋㅋㅋㅋ 기호없이 글만 보여줌!
# #     print("-"*20)

from urllib.request import urlopen
url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'
response=urlopen(url)
source=response.read().decode('utf-8')

print(source[:500])

import json
parsed=json.loads(source)
posts=[]
for d in parsed:
    posts.append(d[{'strDrink'}])

text=''.join(posts)
[print(text)]






# from wordcloud import WordCloud
# wc=WordCloud().generate(text)

# from matplotlib import pyplot

# pyplot.figure(figsize=(12,12))

# pyplot.imshow(wc,interpolation='bilinear')
# pyplot.axis('off')
# pyplot.show()



