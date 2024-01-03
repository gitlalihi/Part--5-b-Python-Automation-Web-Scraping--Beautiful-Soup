# Methods to navigate the tree
import requests
from bs4 import BeautifulSoup
import time

url="http://olympus.realpython.org/profiles/dionysus"
delay_seconds=2
response=requests.get(url)
if response.status_code==200:
    html_content=response.text
    soup=BeautifulSoup(html_content,'html.parser')
    #print(soup.get_text()) # gets text elements
    
    #text_content = soup.get_text()
    #cleaned_text = text_content.replace('\n\n', '\n')# replace the double newlines withe single newline
    #print(cleaned_text) # print the content on terminal
    
    #print(soup.find_all("img")) # gets image links"img src" in form of lists
    
    #print(soup.prettify()) # gets all html format(source code)

    #image1,image2=soup.find_all("img")# gets the actual links from html source code
    #print(image1,image2)
   
    #print(image1["src"])# allows to access the "src"attribute in dictionary notation
    #print(image2["src"])

    #print(soup.title)# prints the title attribute
    #print(soup.title.string)# will print only the string

    #images=soup.find_all("img",src="/static/dionysus.jpg")
    #print(images)
 
    #print(soup.title.parent.name) # prints to ger head of html

    #print(soup.img) # prints the image link on console
    
    time.sleep(delay_seconds)
else:
    print(f'Failed to retrieve content. Status code: {response.status_code}')    

