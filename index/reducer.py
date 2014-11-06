#!/usr/bin/python

import sys
import csv
csv.field_size_limit(sys.maxsize)

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    curterm = None
    references=[]

    for line in reader:
        term, ref = line
        if curterm != term:
            if curterm != None:
                writer.writerow([curterm,','.join(references)])
            curterm = term
            references=[]
        references.extend(ref.split(','))

reducer()
