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
        climberpts = int(rnd["climberpts"])
        # assert (climberpts == 0 or climberpts == 10 or climberpts == 20 or climberpts == 30),"Climber points are invalid! Team %d, round %d." % (int(team), int(rnd["roundnumber"]))
        if (climberpts != 0 and climberpts != 10 and climberpts != 20 and climberpts != 30):
            print "Climber points are invalid! Team %d, round %d." % (int(team), int(rnd["roundnumber"]))