# Test with NavigableString (+more rational and (possibly) more understandable code structure).
from bs4 import BeautifulSoup
from lxml import html


with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    tag1 = soup.p.string #Доступ к строке внутри тега p.
    tag2 = soup.span.string #Доступ к строке внутри тега span.
    print(tag1,end='\n\n') ## Два перевода строки для наглядности вызова результатов.
    print(tag2)

