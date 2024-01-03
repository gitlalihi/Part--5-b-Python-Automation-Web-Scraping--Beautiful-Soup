# to find the title, description and price of a specefic book
# find(),find_all(),find_next() methods
import requests
from bs4 import BeautifulSoup
import time

url='http://books.toscrape.com/catalogue/the-bulletproof-diet-lose-up-to-a-pound-a-day-reclaim-energy-and-focus-upgrade-your-life_931/index.html'

response=requests.get(url)
delay_seconds=5
if response.status_code==200:
    html_content=response.text
    soup=BeautifulSoup(html_content,'html.parser')
    title = soup.find('h1').text.strip()

    # Extract price
    price = soup.find('p', class_='price_color').text.strip()

    # Extract description
    description = soup.find('div', id='product_description').find_next('p').text.strip()

    # Print the extracted information
    print("Title:", title)
    print("Price:", price)
    print("Description:", description)
    time.sleep(delay_seconds)
else:
    print(f'Failed to retreive content.Status code:{response.status_code}')
