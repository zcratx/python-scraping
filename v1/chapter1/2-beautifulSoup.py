from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# bsObj = BeautifulSoup(html, "html.parser")
# print(bsObj.h1)
'''
lxml parser is generally good and ignores missing closing tags
Also this parser is a bit faster
'''
# bsObj1 = BeautifulSoup(html, "lxml")
# print(bsObj1.h1)

bsObj1 = BeautifulSoup(html, "html5lib")
print(bsObj1.h1)
