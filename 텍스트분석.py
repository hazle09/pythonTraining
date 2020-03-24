from urllib.request import urlopen
source=urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')
text=source.read().decode('utf-8')
words=text.split()

from collections import Counter
top5=Counter(words).most_common(5)

from matplotlib import pyplot
top5_words=[t[0] for t in top5]
top5_frequency=[t[1] for t in top5]

pyplot.bar(top5_words, top5_frequency)
pyplot.xlabel('Word')
pyplot.ylabel('Frequency')


pyplot.show()