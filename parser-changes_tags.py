#Замена тэгов средствами BeautifulSoup'а

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)
    tag = soup.span #находим первый в очереди <span>. tag здесь нерезервированное слово.
    tag.name = "div" #меняем <span> на <div>
    
#print(soup)
print(tag)
