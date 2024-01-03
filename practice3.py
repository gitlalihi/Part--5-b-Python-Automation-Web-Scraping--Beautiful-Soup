# To find the list of books that are in stocks from the given url
#find(),find_all(),list comprehension
import requests
from bs4 import BeautifulSoup
import time

url='http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

response=requests.get(url)
delay_seconds=5
if response.status_code==200:
    html_content=response.text
    soup=BeautifulSoup(html_content,'html.parser')
    # Find all list items with the correct class 
    in_stock_items = soup.find_all('article', class_='product_pod')

    # Extract book titles from the in-stock items
    in_stock_books = [item.find('h3').find('a')['title'] for item in in_stock_items]
    print("Books in stock:")
    for book in in_stock_books:
        print(book)
    time.sleep(delay_seconds)
else:
    print(f'Failed to retreive content.Status code:{response.status_code}')