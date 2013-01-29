import json, sys

def rank(j):
    dic = json.loads(j)
    data = dic["data"]
    tags = dic["tags"]
    print data
    
if __name__ == "__main__":
    print sys.argv
    rank(sys.argv[1])
