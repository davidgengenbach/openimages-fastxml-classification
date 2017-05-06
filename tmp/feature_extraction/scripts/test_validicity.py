#!/usr/bin/env python3

from glob import glob

FEATURE_FILES = glob('features.txt')

STEP_SIZE = 10000
counter = 0
for FEATURE_FILE in FEATURE_FILES:
	with open(FEATURE_FILE, 'r') as f:
		found_error = False
		for idx, line in enumerate(f):
			if counter % STEP_SIZE == 0 and counter != 0:
				print('Step: ', counter) 		
			if line.count(',') != 5096 and line.count(',') != 0:
				found_error = True
				print("\tError in {}: Comma count: {} on line {}".format(FEATURE_FILE, line.count(','), line))
			counter += 1
print("Step: ", counter)
print("End!")
