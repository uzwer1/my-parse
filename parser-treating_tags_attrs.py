#Доступ к атрибутам тэгов и замена атрибутов средствами BeautifulSoup'а.

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)
    tag1 = soup.span.attrs #Доступ ко всем атрибутам тега.
    tag2 = soup.span['id'] #Доступ к атрибуту id.
    tag3 = soup.span['class'] #Доступ к атрибуту(-ам) class.
    #tag4 = soup.span['id'] = 'temp' #Доступ к конкретному атрибуту.
    tag4 = soup.span['id'] = 'stamp' #Замена атрибута id своим значением.
#print(soup)
print(tag1)
print(tag2)
print(tag3)
print(tag4)
