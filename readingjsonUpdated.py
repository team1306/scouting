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

highPoints = int(dictionary["data"]["1306"][0]["telehighgoals"])*3
medPoints = int(dictionary["data"]["1306"][0]["telemedgoals"])*2
lowPoints = int(dictionary["data"]["1306"][0]["telelowgoals"])

highPointsAuto = int(dictionary["data"]["1306"][0]["autohighgoals"])*6
medPointsAuto = int(dictionary["data"]["1306"][0]["automedgoals"])*5
lowPointsAuto = int(dictionary["data"]["1306"][0]["autolowgoals"])*4

actualPoints = highPoints+medPoints+lowPoints+highPointsAuto+medPointsAuto+lowPointsAuto
	
print actualPoints

                       
#print(d["data"]["1306"][0]["climberpts"]) #getting specific data