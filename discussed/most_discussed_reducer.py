#!/usr/bin/python

import sys
import csv
from collections import defaultdict

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    # Initialize the vatiables
    id = -1
    discuss = 0


    top = {}

    # if top contains 10 elements replace the smalest value by the actual one.
    def addTop(question,t):
        if len(top) < 10:
            top[question]=t
        else:
            m = min(top, key=top.get)
            if top[m] < t:
                top.pop(m, None)
                top[question]=t;


    # As long as there are lines
    for line in reader:
        # If the key changed
        if id != line[0]:
            # prevent printing the initial vars and only print when key is a number
            if id != -1 and id.isdigit():
                addTop(id,discuss)
            # update vars
            id = line[0]
            discuss = 0
        # add user to the temp var
        if line[0] != 'question' :
            discuss+=1
    # Last line if the Key is a number
    if id.isdigit():
        addTop(id,discuss)

   # Sort top 10 descending by value and write the output
    top = sorted(top.items(), key=lambda x: (-x[1], x[0]))    
    for key in top:
        writer.writerow(key)
reducer()
