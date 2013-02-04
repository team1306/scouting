import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
parser.add_argument("-s", "--shooter", type=float, help="shooter weighting factor", default=1)
parser.add_argument("-c", "--climber", type=float, help="climber weighting factor", default=1)
args = parser.parse_args()

jsonFile = args.file
climberWeight = args.climber
shooterWeight = args.shooter

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
        climberTotal = int(rnd["climberpts"])*climberWeight
        shooterTotal = int(rnd["shootingpts"])*shooterWeight
        temporary.append(climberTotal+shooterTotal)
    teampoints.append([int(team), sum(temporary)/len(temporary)])
    temporary = []

teampoints.sort(key=lambda x: x[1]) #this does the sorting

print teampoints

                       
#print(d["data"]["1306"][0]["climberpts"]) #getting specific data
