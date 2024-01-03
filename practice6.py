# extract all domains (absolute)and relative urls and base_url with links
from urllib.parse import urljoin ,urlparse
from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/'

# Fetch HTML content from the URL
response = requests.get(url)
html_content = response.text

# will parse the url to give its type of scheme(http or https(.scheme)) 
#and its network location(.netloc)

parsed_url = urlparse(url)
domain = parsed_url.scheme + '://' + parsed_url.netloc
print("Domain root is:", domain)

# Get href from all links
links = []
soup = BeautifulSoup(html_content, "html.parser")
for link in soup.find_all('a', href=True):
    # join domain to path
    full_url = urljoin(domain, link['href'])
    links.append(full_url)

# Print output
print('First 5 links are:\n', links[0:5])