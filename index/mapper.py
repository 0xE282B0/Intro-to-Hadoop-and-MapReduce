#!/usr/bin/python

import sys
import csv
import re
from HTMLParser import HTMLParser
csv.field_size_limit(sys.maxsize)

# from stackoverflow http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    # Temp var to store words
    buffer = {}

    for line in reader:
      try:
        # ignore header
        if line[0].isdigit():
            # remove (strip) HTML tags
            parser = MLStripper()
            parser.feed(line[4])
            # For every character chain
            for word in re.findall(r'(\w+)',parser.get_data()):
                # that is longer than 2 chars
                if(len(word) > 3):
                    # save the word as lowercase in a dictionary to be sure it is unique
                    buffer[word.lower()] = line[0]
	# wite all lowercase unique words longer than 2 chars to stdout
        for k, v in buffer.iteritems():
            writer.writerow([k,v])
        # reset buffer
        buffer = {}
      except: 
        sys.stderr.write(str(line))
mapper()
