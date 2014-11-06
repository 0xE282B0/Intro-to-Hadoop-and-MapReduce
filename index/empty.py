#!/usr/bin/python

import sys
import re

import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        writer.writerow(line)


reducer()
