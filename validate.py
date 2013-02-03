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
    for rnd in dictionary["data"][team]:
        assert (int(rnd["climberpts"]) == 0 or int(rnd["climberpts"]) == 10 or int(rnd["climberpts"]) == 20 or int(rnd["climberpts"]) == 30),"Climber points are invalid! Team %d, round %d." % (int(team), int(rnd["roundnumber"]))
