#!/usr/bin/python

import sys
import csv
from datetime import timedelta

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
    
    active = 0
    counter = 0
    longest = 0

    for line in reader:
        activeSecs = float(line[1])
        if activeSecs > longest:
          longest =  activeSecs
        active += activeSecs
        counter += 1
    writer.writerow(["Avarage active time",timedelta(0,active/counter)])
    writer.writerow(["Longest active time",timedelta(0,longest)])

reducer()
