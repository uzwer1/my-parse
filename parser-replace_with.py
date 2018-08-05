# Test with NavigableString and replace_with()
from bs4 import BeautifulSoup
from lxml import html


with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    tag1 = soup.p.string #Доступ к строке внутри тега p.
    soup.p.string.replace_with('No longer bold')#Замена строки внутри тега p на уровне Soup'а.
    tag2 = soup.p.string #Доступ к новой версии строки.
    print(tag1,end='\n\n')
    print(tag2,end='\n\n')
    
