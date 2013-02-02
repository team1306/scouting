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
x = 0
temporary = [] #add up a teams points per round here temporarily
teampoints = [] #a big list with all teams and their average points

for team in dictionary["data"]:
    for rnd in dictionary["data"][team]:
        temporary.append(int(rnd["climberpts"])+int(rnd["shootingpts"]))
    teampoints.append([team, sum(temporary)/len(temporary)])
    temporary = []

teampoints.sort(key=lambda x: x[1]) #this does the sorting

print teampoints

                       
#print(d["data"]["1306"][0]["climberpts"]) #getting specific data
