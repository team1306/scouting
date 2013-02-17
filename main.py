import csvtojson, ranking, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="~/MC-Projects/AMCscouting2013/exports/AMCscouting2013.csv")
parser.add_argument("-s", "--shooter", type=float, help="shooter weighting factor", default=1)
parser.add_argument("-c", "--climber", type=float, help="climber weighting factor", default=1)

args = parser.parse_args()

print ranking.rank(csvtojson.csvtojson(args.file), args.climber, args.shooter)
