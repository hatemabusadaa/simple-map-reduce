#!/usr/bin/env python3

import sys

current_file =None
current_count = 0
file = None


for line in sys.stdin:
	line=line.strip()
	file, count = line.split('\t',1)
	
	count=int(count)
	
	if current_file==file:
		current_count= current_count + count
	else:
	     if current_file:
	         print('%s\t%s' % (current_file, current_count))
	     current_count=count
	     current_file=file
	     
if current_file == file:
	print('%s\t%s' % (current_file, current_count))
