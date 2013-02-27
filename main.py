import csvtojson, ranking, argparse

# parse the tags to get the name of the input file and the respective climbing and shooting weights
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="./AMCscouting2013.csv")
parser.add_argument("-s", "--shooter", type=float, help="shooter weighting factor", default=1)
parser.add_argument("-c", "--climber", type=float, help="climber weighting factor", default=1)

args = parser.parse_args()

# print the resulting ranking
print ranking.rank(csvtojson.csvtojson(args.file), args.climber, args.shooter)
