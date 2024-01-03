# to understand parent,children and siblings in a DOM and get the result
from bs4 import BeautifulSoup

# Your HTML content
html_content = """
content from books.toscrape.com

"""

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Open a new file to write the extracted text
with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    # Extract text from parents
    for parent in soup.find_all(['header', 'div', 'form']):
        parent_text = parent.get_text(strip=True)
        if parent_text:
            file.write(f'Parent Text: {parent_text}\n\n')

    # Extract text from children
    for parent in soup.find_all(['header', 'div', 'form']):
        for child in parent.find_all():
            child_text = child.get_text(strip=True)
            if child_text:
                file.write(f'Child Text: {child_text}\n')

    # Extract text from siblings
    for sibling in soup.find_all(['a', 'p', 'h3']):
        sibling_text = sibling.get_text(strip=True)
        if sibling_text:
            file.write(f'Sibling Text: {sibling_text}\n')

print("Text extraction completed. Check 'extracted_text.txt' for the results.")