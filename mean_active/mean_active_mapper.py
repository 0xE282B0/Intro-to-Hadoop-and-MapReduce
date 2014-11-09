#!/usr/bin/python

import sys
import csv
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    # As long as there are lines
    for line in reader:
	if len(line) == 19 and line[0].isdigit() and line[5] == 'question':
          try:
            writer.writerow([line[0],(datetime.strptime(line[13][0:-10], "%Y-%m-%d %H:%M:%S")-datetime.strptime(line[8][0:-10], "%Y-%m-%d %H:%M:%S")).total_seconds()])
          except:
            pass
mapper()
