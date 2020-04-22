from urllib.request import urlopen
url='https://jsonplaceholder.typicode.com/posts?userId=1'
response=urlopen(url)
source=response.read().decode('utf-8')

import json
parsed=json.loads(source)
posts=[]
for d in parsed:
    posts.append(d['body'])

text=''.join(posts)

from wordcloud import WordCloud
wc=WordCloud().generate(text)

from matplotlib import pyplot

pyplot.figure(figsize=(12,12))

pyplot.imshow(wc,interpolation='bilinear')
pyplot.axis('off')
pyplot.show()



