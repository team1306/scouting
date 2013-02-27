import json
import argparse


def rank(dictionary, climberWeight, shooterWeight):
    dictionarylength = (len(dictionary["data"]))

    x = 0
    temporary = [] #add up a teams points per round here temporarily
    teampoints = [] #a big list with all teams and their average points

    for team in dictionary["data"]:
        print team
        for rnd in dictionary["data"][str(team)]:
            print rnd
            climberTotal = int(rnd["climbingpts"][2:])*climberWeight
        
            
            highPoints = int(rnd["telehighgoals"])*3
            medPoints = int(rnd["telemedgoals"])*2
            lowPoints = int(rnd["telelowgoals"])
            
            highPointsAuto = int(rnd["autohighgoals"])*6
            medPointsAuto = int(rnd["automedgoals"])*5
            lowPointsAuto = int(rnd["autolowgoals"])*4      
            
            shooterTotal = (highPoints+medPoints+lowPoints+highPointsAuto+medPointsAuto+lowPointsAuto)*shooterWeight
            temporary.append(climberTotal+shooterTotal)
        teampoints.append([int(team), sum(temporary)/len(temporary)])
        temporary = []

        teampoints.sort(key=lambda x: x[1]) #this does the sorting

        return teampoints

if __name__ == "__main__":
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
    print rank(dictionary, climberWeight, shooterWeight)
