#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    # As long as there are lines
    for line in reader:
        # Use tags for questions only (remove this line to use all tags
            # Write each Tag 
            if line[3].isdigit():
                writer.writerow([line[3], line[5]])
mapper()
