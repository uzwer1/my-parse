#Удаление атрибутов тэгов на уровне soup'а.

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)
    tag = soup.span.attrs #Доступ ко всем атрибутам тега.
    del soup.span['class'] #Удаление на уровне soup'а атрибута class.
    del soup.span['id'] #Удаление на уровне soup'а атрибута id.
print(tag)
