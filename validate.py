import json
import sys

jsonFile = sys.argv[1]

jsonFileLines = open(jsonFile)
lines = jsonFileLines.readlines()
jsonFileLines.close()

s = ""
for line in lines:
    s += line.strip("\n")

dictionary = (json.loads(s)) #this is the dictionary
dictionarylength = (len(dictionary["data"]))
temporary = [] #add up a teams points per round here temporarily
teampoints = [] #a big list with all teams and their average points

for team in dictionary["data"]:
    # We could add a teams dictionary and have it say when teams don't exist.
    for rnd in dictionary["data"][team]:
        # Climber points can now only be valid values by the sheet.
        # Shooting points cannot be validated.
        # Round number could be validated as needing to be a legal round number, but that's silly since round numbers don't actually matter.
        # Autonomous points might be validatable, but we will have to consider whether it's worth it.
        break
        