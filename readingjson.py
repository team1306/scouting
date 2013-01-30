import json

f = open('exampleData.json')
lines = f.readlines()
f.close()

s = ""
for line in lines:
    s += line.strip("\n")

dictionary = (json.loads(s)) #this is the dictionary

dictionarylength = (len(dictionary["data"])) #number of items in dictionary
x = 0
temporary = [] #add up a teams points per round here temporarily
teampoints = [] #a big list with all teams and their average points

for team in dictionary["data"]:
    for rnd in dictionary["data"][team]:
        temporary.append(int(rnd["climberpts"])+int(rnd["shootingpts"]))

print temporary


                       
#print(d["data"]["1306"][0]["climberpts"]) #getting specific data

string = "12"
