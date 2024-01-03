# Repeat Practice for fetching parent, children and siblings in a HTML DOM
from bs4 import BeautifulSoup

# Your HTML content
html_content = '''
<html>
<head>
<TITLE>Profile: Dionysus</TITLE>
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/dionysus.jpg" />
<h2>Name: Dionysus</h2>
<img src="/static/grapes.png"><br><br>
Hometown: Mount Olympus
<br><br>
Favorite animal: Leopard <br>
<br>
Favorite Color: Wine
</center>
</body>
</html>'''

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Open a new file to write the extracted text
with open('extracted_text2.txt', 'w', encoding='utf-8') as file:
    # Extract text from parents
    for parent in soup.find_all(['head', 'body']):
        parent_text = parent.get_text(strip=True)
        if parent_text:
            file.write(f'Parent Text: {parent_text}\n\n')

    # Extract text from children
    for parent in soup.find_all(['head', 'body']):
        for child in parent.find_all():
            child_text = child.get_text(strip=True)
            if child_text:
                file.write(f'Child Text: {child_text}\n')

    # Extract text from siblings
    for sibling in soup.find_all(['img', 'h2', 'br', 'p']):
        sibling_text = sibling.get_text(strip=True)
        if sibling_text:
            file.write(f'Sibling Text: {sibling_text}\n')

print("Text extraction completed. Check 'extracted_text2.txt' for the results.")