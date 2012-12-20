Scouting by Team 1306
========

##License
Copyright 2012 by Contributors

Licensed under the [GPLv3](http://www.gnu.org/licenses/gpl.txt).

## Components

### getschedule.py

`getschedule.py` was created to download and parse the match schedules posted by FIRST at the beginning of a tournament. It takes in arguments of the schedule URL and a team number, and outputs a list of teams which do not share matches with the input team.

We plan to expand it to instead take a list of teams and output an array containing scouting teams and the teams for them to scout.

### csvtojson.py

`csvtojson.py` was created to interface with [Auto Multiple Choice](http://home.gna.org/auto-qcm/) and convert the CSV files exported by AMC to a JSON of data, sorted by teams. This JSON can then be run through a team's algorithms to find ideal alliance partners.