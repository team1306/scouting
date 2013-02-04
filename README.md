Scouting by Team 1306
========

##License
Copyright 2012 by Contributors

Licensed under the [GPLv3](http://www.gnu.org/licenses/gpl.txt).

## Components

### exampledata.json

`exampledata.json` is our test data file for all of the scripts. It contains data meant to test all of our scripting, though it is not a complete simulation of a tournament (such a simulation will be provided by either randomly generated or previous tournament data.)

### getschedule.py

`getschedule.py` was created to download and parse the match schedules posted by FIRST at the beginning of a tournament. It takes in arguments of the schedule URL and a team number, and outputs a list of teams which do not share matches with the input team.

We plan to expand it to instead take a list of teams and output an array containing scouting teams and the teams for them to scout.

### csvtojson.py

`csvtojson.py` was created to interface with [Auto Multiple Choice](http://home.gna.org/auto-qcm/) and convert the CSV files exported by AMC to a JSON of data, sorted by teams. This JSON can then be run through a team's algorithms to find ideal alliance partners.

### readingjson.py

`readingjson.py` takes the JSON that is produced by the aformentioned `csvtojson.py` and runs it through a scoring algorithm, then sorts the results by the score according to the algorithm. It uses argparse to have flags with arguments, so `-f` specifies the input JSON file, `-s` specifies the shooting point weight, and `-c` specifies the climbing point weight.

### validate.py

`validate.py` validates the data in the file used as an argument. Currently, it makes sure the climbing points are a possible score, though we'll expand the validation as necessary.