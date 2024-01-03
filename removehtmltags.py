# to remove html tags using decompose() method
#import requests
from bs4 import BeautifulSoup

html_content='''
<p>In the United States, website owners can use three major 
<a href="/wiki/Cause_of_action" title="Cause of action">legal claims</a> 
to prevent undesired web scraping: (1) copyright infringement (compilation),
(2) violation of the <a href="/wiki/Computer_Fraud_and_Abuse_Act" title="Computer Fraud and 
Abuse Act">Computer Fraud and Abuse Act</a> ("CFAA"), and (3) <a href="/wiki/Trespass_to_chattels"
title="Trespass to chattels">trespass to chattel</a>.<sup id="cite_ref-6" class="reference">
<a href="#cite_note-6">[6]</a></sup> However, the effectiveness of these claims 
relies upon meeting various criteria...</p>'''

soup = BeautifulSoup(html_content, 'html.parser')
par = soup.find_all('p')[0]

# Get all links
links = par.find_all('a')
print(links)

# Remove references from tags- refernced with ,<sup>
par.find('sup').decompose()
links_after_removal = par.find_all('a')
print(links_after_removal)