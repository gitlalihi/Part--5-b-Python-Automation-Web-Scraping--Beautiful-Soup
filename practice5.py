#Practice step by step
# to extract content from the web- page
# Name of the website to scrape-http://books.toscrape.com/


import requests
url="http://books.toscrape.com/"
response = requests.get(url)
print('Status code: ', response.status_code)
html_content=response.text



# to parse using beautifulsoup class

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# Extract any HTML tag
#print(soup.find('title'))

#Find elemets by tag name
# Extracting HTML tags

#title = soup.find('title')
#h1 = soup.find('h1')

#print("Your links is ")
# To extract links
'''for l in soup.find_all('a'):
    link=url+l.get('href')
    print(link)'''

# Print the outputs
#print('Title: ', title)
#print('h1: ', h1)

#Find Elements by ID
#print(soup.find(id="default"))

# Find elements by class
#books=soup.find_all('ul',class_='nav nav-list')
#print(books)

# Find elements with CSS selectors
'''for b in books:
    name=b.select('.side categories ,.nav-list li ul li a')
    print(name)'''

# To extract from HTML elements
'''categories_list=soup.select('.side_categories .nav-list  li ul li a') 
for c in categories_list: 
    print(c.text.strip())'''

#Using attributes
# Parsing using HTML tag attributes
'''create_date = soup.find('meta', attrs={'name':'created'})
meta_robots =  soup.find('meta', attrs={'name':'robots'})
print('Created_date: ',create_date)
print('meta robots: ',meta_robots)'''

#Parsing unavailable tags else print none
# Extract the title tag
'''title_tag = soup.title
print(f'Title: {title_tag.text.strip()}') if title_tag else print('Title tag not found')'''

# Extract meta tags
'''meta_tags = soup.find_all('meta')
for meta_tag in meta_tags:
    print(f'Meta Tag - Name: {meta_tag.get("name")}, Content: {meta_tag.get("content")}') if meta_tags else print('No meta tags found')'''

# Extract links to stylesheets
'''stylesheet_links = soup.find_all('link', {'rel': 'stylesheet'})
for link in stylesheet_links:
    print(f'Stylesheet Link: {link.get("href")}') if stylesheet_links else print('No stylesheet links found')'''


# Extracting textual content using string methods tofind the exact descreiption
'''soup = BeautifulSoup(html_content, 'html.parser')
meta_tags = soup.find_all('meta', attrs={'name': 'description'})
print(meta_tags)'''

# Using user-defined functions to soup object by listing out links to stylesheets

'''def list_stylesheets(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('link', rel='stylesheet')
    stylesheet_list = []
    for link in links:
        href = link.get('href')
        stylesheet_list.append(href)
    return stylesheet_list

# Use the user-defined function
stylesheets = list_stylesheets(html_content)

# Print the results
print("Stylesheets:")
for stylesheet in stylesheets:
    print(stylesheet)'''

# Find Parents
'''a_child = soup.find_all('a')[0]
print(a_child.find_parent())
print(a_child.find_parents())


#Find children
a_child = soup.find_all('a')[0]
print(a_child.findChild())
print(a_child.findChildren())
#or
print(list(a_child.children))'''

#find siblings
'''a_child = soup.find('a')
print(a_child.find_next_sibling())
print(a_child.find_next_siblings())'''

# write the source code to an output file
with open('extracted_file.html', 'w', encoding='utf-8') as file:
    pretty_soup = soup.prettify()
    file.write(pretty_soup)

