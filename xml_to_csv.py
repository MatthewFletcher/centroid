#Strip xml data and create csv text file

import csv

with open("teststatedata.txt", "r") as statedataFile:
	statedataReader = csv.reader(statedataFile)
	x,y=[],[]

	for row in statedataReader:
		if len(row) != 0: 
			cleanstatedata=statedataReader[13:]
