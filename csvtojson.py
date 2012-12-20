import json, sys

f = open(sys.argv[1], 'r')

lines = f.readlines()
csv = []
for line in lines:
    csv.append(line.replace('"', '').replace('\n', '').split(';'))

dic = {'tags': csv[0]}
csv.pop(0)
l = []
d = {}
for x in range(len(csv)):
    for i in range(len(dic['tags'])):
        d[dic['tags'][i]]=csv[x][i]
    l.append(d)
dic['data'] = l

j = json.dumps(dic)

print j
