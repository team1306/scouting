import json, sys

f = open(sys.argv[1], 'r') # open file specified by the first argument to the function

lines = f.readlines() # read raw data into list
csv = []
for line in lines:
    csv.append(line.replace('"', '').replace('\n', '').split(';')) # read lines of CSV into 2 x (number of tags) list ignoring quotes and newlines and spliting at semicolons

l = []
for tag in csv[0]: # take only the tags that contain more than a single digit
    if '.' not in tag:
        l.append(tag)
dic = {'tags': l} # assign tags to the list of important tags
d = {}

i=0
while i < len(csv[0]): # loop through the tags and assign tags to their values
    while '.' in csv[0][i]: # just keep going if the tag contains a '.'
        i += 1
    if i >= len(csv[0]): # make sure we haven't overshot the lenth of the list before trying to access it
        break
    d[csv[0][i]] = csv[1][i] # set key for tag to its value
    i += 1
dic['data'] = d # add dictionary to data tag in the main one

j = json.dumps(dic) # convert dictionary to JSON

print j

