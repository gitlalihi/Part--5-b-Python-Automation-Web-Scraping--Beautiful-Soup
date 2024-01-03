'''To extract a list of all the links on the page by 
looking for HTML tags with the name a and retrieving the 
value taken on by the href attribute of each tag.'''
#get(),find_all()
import requests
from bs4 import BeautifulSoup
import time

url='http://olympus.realpython.org/profiles'
delay_seconds=5
response=requests.get(url)
if response.status_code==200:
    html_content=response.text
    soup=BeautifulSoup(html_content,'html.parser')
    for l in soup.find_all('a'):
        link=url+l.get('href')
        print(link)
    time.sleep(delay_seconds)
else:
    print(f'Failed to retrive content.Status code : {response.status_code}')        

