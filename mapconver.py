#! /usr/bin/python3

import sys 

for line in sys.stdin:
	line=line.strip()
	product_act,product_name = line.split(',')[2:]
	
	print(f"{product_name}\t{product_act}")

