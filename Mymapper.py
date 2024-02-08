#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line=line.strip()
	file_name=line.split()[3]
	
	print('%s\t%s'%(file_name,1))

