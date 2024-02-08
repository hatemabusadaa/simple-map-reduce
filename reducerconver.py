#! /usr/bin/python3

import sys 

current_product =None
total_pur=0.0
total_view=0.0

for line in sys.stdin:
	line = line.strip()
	product_name,product_act = line.split('\t')
	
	if current_product != product_name:
		if current_product:
			conevrsion_rate=total_pur/total_view
			print(f"{current_product}\t{conevrsion_rate}")
		current_product = product_name
		total_pur= 0.0
		total_view=0.0
		
	# acc rev for the current 
	if product_act=='view':
		total_view=total_view+1
	if product_act=='purchase':
		total_pur=total_pur+1	
	
if current_product:
	conevrsion_rate=total_pur/total_view
	print(f"{current_product}\t{conevrsion_rate}")
	

