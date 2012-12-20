import urllib
from lxml import html

url = "http://www2.usfirst.org/2012comp/events/WI/schedulequal.html"
page = html.fromstring(urllib.urlopen(url).read())

l = []
for x in page.xpath("//td"):
    if x.text_content()[0] != "\r":
        l.append(x.text_content())

matches = []
while len(l) > 0:
    match = []
    for i in range(8):
        match.append(l.pop(0))
    matches.append(match)

teams = []
for i in range(len(matches)):
    for x in range(2,8):
        if matches[i][x] not in teams:
            teams.append(matches[i][x])

conflicts = {}
for i in range(len(teams)):
    conflicts[teams[i]] = []
    for x in range(len(matches)):
        if teams[i] in matches[x][2:8]:
            for y in range(2,8):
                if matches[x][y] not in conflicts[teams[i]]:
                    conflicts[teams[i]].append(matches[x][y])
            
good = {}
for i in range(len(teams)):
    good[teams[i]] = []
    for x in range(len(teams)):
        if i != x and teams[x] not in conflicts[teams[i]]:
            good[teams[i]].append(teams[x])

print good['1306']
