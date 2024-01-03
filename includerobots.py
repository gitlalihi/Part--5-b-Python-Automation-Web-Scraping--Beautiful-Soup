import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
import time

url = "http://olympus.realpython.org/profiles/dionysus"
delay_seconds = 2

# Parse the robots.txt file
rp = RobotFileParser()
rp.set_url(url + "/robots.txt")
rp.read()

# Check if the user agent is allowed to fetch the URL
if rp.can_fetch("*", url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # Scraping Logic
        text_content = soup.get_text()
        cleaned_text = text_content.replace('\n\n', '\n')# replace the double newlines withe single newline
        print(cleaned_text) # print the content on terminal
        
        time.sleep(delay_seconds)
    else:
        print(f'Failed to retrieve content. Status code: {response.status_code}')
else:
    print(f'Access to {url} is not allowed according to robots.txt')
