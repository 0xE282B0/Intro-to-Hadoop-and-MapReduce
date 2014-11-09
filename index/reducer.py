#!/usr/bin/python

import sys
import csv
# The second column can be very huge.
csv.field_size_limit(sys.maxsize)

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    curterm = None
    references=[]

    for line in reader:
        term, ref = line
        # If the key changes
        if curterm != term:
            if curterm != None:
                # Write all ids coma separated.
                writer.writerow([curterm,','.join(references)])
            curterm = term
            references=[]
        # Save current id[s]
        references.extend(ref.split(','))

reducer()
