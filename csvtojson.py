import json, sys, argparse

def goodtags(t):
    good = []
    for tag in t[0]:
        if tag[-2:-1] != '.':
            good.append(tag)
        if tag[-2:] == '.1': # if there is only once column in an AMCcode, it will just export <code>.1, but if there are multiple codes, they are aggregated in <code>
            for i in range(len(t[0])):
                if t[0][i] == tag[:-2]:
                    break
                if i == len(t[0]) - 1:
                    good.append(tag)
    return good

def csvtojson(f):
    f = open(f, 'r') # open file specified by the first argument to the function

    lines = f.readlines() # read raw data into list
    csv = []
    for line in lines:
        csv.append(line.replace('"', '').replace('\n', '').split(';')) # read lines of CSV into 2 x (number of tags) list ignoring quotes and newlines and spliting at semicolons

    l = goodtags(csv)
    
    dic = {'tags': l} # assign tags to the list of important tags

    data = {} # create data dictionary to be indexed by team number and list of teams for which lists have already been created
    teams = []
    
    for match in [x + 1 for x in range(len(csv)-1)]: # loop through for every line of data
        d = {}
        i = 0
        while i < len(csv[0]): # loop through the tags and assign tags to their values
            while csv[0][i] not in l: # just keep going if the tag isn't a good tag
                i += 1
            if i >= len(csv[0]): # make sure we haven't overshot the lenth of the list before trying to access it
                break
            d[csv[0][i]] = csv[match][i] # set key for tag to its value
            i += 1
        if d['teamnumber'] not in teams: # add a list of match data for a team if none exists
            data[d['teamnumber']] = []
            teams.append(d['teamnumber']) # store the teamnumber so that we know a list exists
        data[d['teamnumber']].append(d) # and add the data to the list

    dic['data'] = data # add dictionary to data tag in the main one
        

    return dic # convert dictionary to JSON

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    print csvtojson(args.file) # run function with command line argument

