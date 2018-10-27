# coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import nltk
from nltk.corpus import stopwords
import matplotlib

response = urllib2.urlopen("https://php.net")
html = response.read()

soup = BeautifulSoup(html, "html5lib")
# 这里需要安装html5lib模块

text = soup.get_text(strip = True)
tokens = text.split()
clean_tokens = list()
sr = stopwords.words("english")

for token in tokens:
	if not token in sr:
		clean_tokens.append(token)

freq = nltk.FreqDist(clean_tokens)

for key, val in freq.items():
	
	print "%s" % key + ":" + "%s" % val

freq.plot(20, cumulative = False)
