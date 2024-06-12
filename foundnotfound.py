import re
from urllib.request import urlopen
import requests

'''Open Broadcom support knowledge article.'''
url = input("What knowledge article are you needing to check?")
# Present yourself to support.broadcom.com as a Firefox iPad, because presenting as apython script is not supported
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

r = requests.get(url, headers=HEADERS)

hrefs = re.findall('<a href=.*?</a>', r.text)
hrefList = ""

for h in hrefs:
    if '://' in h:
        hrefList += h + "\n"
print("\nLinks found: \n" + hrefList) 