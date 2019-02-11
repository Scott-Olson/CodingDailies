# uniformly pick a random element from an infinite stream

import random

def pick(big_stream):
	random_element = None

	# We want K to have 1 / (i + 1) chance of being chosen after the iteration. This is the case since the chance of having being chosen already but not getting swapped with the ith element is 1 / i * (1 - (1 / (i + 1))) which is 1 / i * i / (i + 1) or 1 / (i + 1)

	for i, e in enumerate(big_stream):
		if i == 0:
			random_element = e
		if random.randint(1,i + 1) == 1:
			random_element = e
	return random_element