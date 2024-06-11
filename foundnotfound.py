import re, csv
from datetime import datetime
from urllib.request import urlopen

'''Open Broadcom support knowledge article.'''
url = input("What knowledge article are you needing to check?")
page = urlopen(url)
html = page.read().decode("utf-8")

# #csv file creation
# filename = (str(datetime.now())[:+19]).replace(":", "").replace("-", "").replace(" ", "_") + '.csv'
# header = ['StoryType', 'StoryID', 'StoryKHeadline']
# data = []
# #StoryType can be RS or OS, related stories or other stories

# Get all url's within a "wolken-content-container" div
body = "wolken-content-container.*?>.*Was this article helpful?"
rs_results = re.findall(body, html, re.IGNORECASE)
print(rs_results)
# y = 0

# #cleanup output and print
# print("Related Stories:" + "\n")
# if (len(rs_results) ==8):
#     rs_results = rs_results[4:8]
# for x in rs_results:
#     title = re.sub("<.*?>", "", x)
#     title = title.removeprefix("BigLittle-title\">")
#     y = y+1
#     data.append([ "RS", y, title])
#     print(title)

# #Get the other stories
# pattern = "ListItem-title.*?>.*</h3>"
# os_results = re.findall(pattern, html, re.IGNORECASE)
# y = 0

# #print("\n\nOther Stories:" + "\n")
# for x in os_results:
#     title = re.sub("<.*?>", "", x)
#     title = title.removeprefix("ListItem-title\">")
#     y = y + 1
#     data.append([ "OS", y, title])
#     print(title)

# #write the data to a csv
# with open(filename, 'w') as file:
#     for header in header:
#         file.write(str(header)+', ')
#     file.write('\n')
#     for row in data:
#         for x in row:
#             file.write(str(x)+', ')
#         file.write('\n')

# time = datetime.now()
# local_now = time.astimezone()  #local_now is the local time with the UTC offset, signifying timezone
# local_tz = local_now.tzinfo
# time = str(time)[:-7]
# #print(time, local_tz)

# #print(filename)
