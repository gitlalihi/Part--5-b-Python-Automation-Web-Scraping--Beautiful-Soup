# to check access for scraping site with robots.txt 
import requests
from urllib import robotparser
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time

def fetch_robots_txt(base_url):
    robots_url = urljoin(base_url, '/robots.txt')
    response = requests.get(robots_url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch robots.txt. Status code: {response.status_code}")
        return None

def parse_robots_txt(robots_content):
    rp = robotparser.RobotFileParser()
    rp.parse(robots_content.splitlines())
    return rp

def can_fetch_url(rp, user_agent, url):
    return rp.can_fetch(user_agent, url)

def main():
    base_url = 'https://crawler-test.com'
    user_agent = '*'

    # Step 1: Fetch robots.txt
    robots_content = fetch_robots_txt(base_url)

    if robots_content:
        # Step 2: Parse robots.txt
        rp = parse_robots_txt(robots_content)

        # Step 3: Check if the bot is allowed to access a specific URL
        sample_url = urljoin(base_url, 'https://crawler-test.com')
        if can_fetch_url(rp, user_agent, sample_url):
            with requests.Session() as session:
                # Adding a delay to the server
                delay_seconds = 5
                response = session.get(sample_url)
                if response.status_code == 200:
                    print(f"Scraping  allowed for {sample_url}")
                    html_content = response.text
                    soup = BeautifulSoup(html_content, 'html.parser')
                    print(soup.prettify())
                    time.sleep(delay_seconds)
                else:
                    print(f"Failed to fetch {sample_url}. Status code: {response.status_code}")
        else:
            print(f"Access to {sample_url} is not allowed by robots.txt")

if __name__ == "__main__":
    main()