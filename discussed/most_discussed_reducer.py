#!/usr/bin/python

import sys
import csv
from collections import defaultdict

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    # Initialize the vatiables
    id = -1
    user = []

    # As long as there are lines
    for line in reader:
        # If the key changed
        if id != line[0]:
            # prevent printing the initial vars and only print when key is a number
            if id != -1 and id.isdigit():
                writer.writerow([id,user])
            # update vars
            id = line[0]
            user = []
        # add user to the temp var
        user.append(line[1])
    # Last line if the Key is a number
    if id.isdigit():
        writer.writerow([id,user])

reducer()
