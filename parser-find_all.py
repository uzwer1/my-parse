# First method to get all the tags, not only the first as it was before.
from bs4 import BeautifulSoup
from lxml import html

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    tag = soup.find_all('span') #First appearance find_all()
    for child in tag: #Loop for 'child' aka 'all span'.
        print(child.contents,end='\n\n') #Separate by .contents soup from variable named 'tag'.
    
    
