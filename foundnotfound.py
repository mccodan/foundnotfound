import re
from urllib.request import urlopen
import requests

'''Open Broadcom support knowledge article.'''
url = input("What knowledge article are you needing to check?")
# Present yourself to support.broadcom.com as a Firefox iPad
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

r = requests.get(url, headers=HEADERS)



hrefs = re.findall('<a href=.*?</a>', r.text)
#<a href="https://kb.vmware.com/s/article/1002282" target="_blank">KB 1002282</a>

hrefList = ""

# need to make a list of 2 property objects: url and <a> text
for h in hrefs:
    # if h contains "https://" add everything between "" to list                         <---- add the link
    if '://' in h:
        hrefList += h + "\n"
    # if line contains </a>, get everything between first "> and </a> to get the text    <---- add the text
print("\nLinks found: \n" + hrefList) 

# linkList = "Links: "
# for h in hrefList:
#     if '"' in h:
#         linkList += re.search(".*?", h)

# print(linkList)
# linkList = ""
# build the 2 property list