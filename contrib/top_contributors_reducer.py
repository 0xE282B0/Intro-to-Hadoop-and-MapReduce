#!/usr/bin/python

import sys
import csv
import time
from datetime import datetime, timedelta


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    top = {}

    # if top contains 10 elements replace the smalest value by the actual one.
    def addTop(i,cont):
        if len(top) < 10:
            top[i]=cont
        else:
            m = min(top, key=top.get)
            if top[m][0] < cont[0]:
                top.pop(m, None)
                top[i]=cont;

    # initialize the variables
    current = None
    question =0
    answer =0
    comment =0
    
    # As long as there are lines
    for line in reader:
        uid , typ = line

        # if key changes
        if current != uid:
            # prevent adding initial vars
            if current != None:
                addTop(current,[question+answer+comment,question,answer,comment])
            # update key and reset counter
            current = uid
            question =0
            answer =0
            comment =0
        if typ == "answer":
            question += 1
        elif typ == "question":
            answer += 1
        elif typ == "comment":
            comment += 1
    # Add last line
    addTop(current,[question+answer+comment,question,answer,comment])

    # Sort top 10 descending by value and write the output
    top = sorted(top.items(), key=lambda x: (-x[1][1], x[1][0]))    
    for key in top:
        writer.writerow(key)

reducer()
