# Web-scraping pratice
# To list all categories of books  from the given url
#select()- CSS selector

import requests
from bs4 import BeautifulSoup
import time

url='http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
delay_seconds=5
response=requests.get(url)
if response.status_code==200:
    html_content=response.text
    soup=BeautifulSoup(html_content,'html.parser')
    print("The list of category of books are")
    categories_list=soup.select('.side_categories .nav-list  li ul li a') # Select all categoreies of list that  are of children of  class nav-list
    for c in categories_list: # print list of categories of books
        print(c.text.strip())
    
    time.sleep(5)    
else:
    print(f'Failed to retrive content.Status code : {response.status_code}')
