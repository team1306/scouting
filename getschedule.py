import urllib
from lxml import html # lxml is our html parsing library
import sys

url = sys.argv[1] # Run the script with the url as the first argument.
page = html.fromstring(urllib.urlopen(url).read()) # Makes a local copy of the HTML source

l = [] # This just creates an array of the cells in the table found on the website.
for x in page.xpath("//td"):
    if x.text_content()[0] != "\r":
        l.append(x.text_content())

matches = [] # Creates an array of the match info, separated into matches.
while len(l) > 0:
    match = []
    for i in range(8): # Divides l (the info from the website) into 8 piece chunks
        match.append(l.pop(0)) # Appends the elements into match
    matches.append(match) # Then appends match into matches, creating the subarrays inside matches

teams = [] # Creates a list of the teams
for i in range(len(matches)):
    for x in range(2,8): # Looks for the appropriate elements in the subarrays (the elements that are teams)
        if matches[i][x] not in teams: # If they aren't in the team list
            teams.append(matches[i][x]) # They get added.

conflicts = {} # Creates a dictionary of teams which play at the same time as other teams
for i in range(len(teams)):
    conflicts[teams[i]] = []
    for x in range(len(matches)):
        if teams[i] in matches[x][2:8]: # Scans through the matches subarrays to see if a team is in the match.
            for y in range(2,8): # If it is,
                if matches[x][y] not in conflicts[teams[i]]: # And it's not already in the dictionary,
                    conflicts[teams[i]].append(matches[x][y]) # It adds it to the dictionary

good = {} # Creates a dictionary of teams which never play at the same time
for i in range(len(teams)):
    good[teams[i]] = []
    for x in range(len(teams)):
        if i != x and teams[x] not in conflicts[teams[i]]: # Checks if a team is not in the conflicts dictionary.
            good[teams[i]].append(teams[x]) # If it isn't, adds it to the good dictonary.

times = {} # Creates a dictionary of the times a team plays at
for i in range(len(teams)):
    times[teams[i]] = []
    for x in range(len(matches)):
        if teams[i] in matches[x][2:8]: # Checks if a team is in a specific matches subarray
            times[teams[i]].append(matches[x][0]) # If it is, appends the time to the dictionary

teammatches = {} # Much like times, except uses match numbers since they're more reliable
for i in range(len(teams)):
    teammatches[teams[i]] = []
    for x in range(len(matches)):
        if teams[i] in matches[x][2:8]:
            teammatches[teams[i]].append(matches[x][1]) # Appends match number to dictionary

