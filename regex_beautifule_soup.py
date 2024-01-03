# using regex with bs4


import re
from bs4 import BeautifulSoup

html_content = """
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="created" content="24th Jun 2016 09:29">
<meta name="description" content="">
<meta name="viewport" content="width=device-width">
<meta name="robots" content="NOARCHIVE,NOCACHE"><!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
<!--[if lt IE 9]>
    <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
<link rel="shortcut icon" href="../../../static/oscar/favicon.ico">
<link rel="stylesheet" type="text/css" href="../../../static/oscar/css/styles.css">
<link rel="stylesheet" href="../../../static/oscar/js/bootstrap-datetimepicker/bootstrap-datetimepicker.css">
<link rel="stylesheet" type="text/css" href="../../../static/oscar/css/datetimepicker.css">
"""

def filter_stylesheets(tag):
    # Custom function to filter <link> elements with 'rel'='stylesheet' and 'href' matching the pattern
    return tag.name == 'link' and tag.get('rel') == ['stylesheet'] and re.search(r'\.css$', tag.get('href'))

def list_stylesheets_with_regex(html, filter_func):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Pass the filter function to find_all
    links = soup.find_all(filter_func)
    
    stylesheet_list = [link.get('href') for link in links]
    return stylesheet_list

# Use the user-defined function with the filter function
stylesheets = list_stylesheets_with_regex(html_content, filter_stylesheets)

# Print the results
print("Stylesheets:")
for stylesheet in stylesheets:
    print(stylesheet)
