# 1/12/2018
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

test_set_1 = [3, 4, -1, 1] #should return 2
test_set_2 = [1, 2, 0] #should return 3
def missing_poss(arr):
	lowest_int: int
	for i in range(0, len(arr)):
		if arr[i] <= 0:
			pass
		if lowest_int:
			lowest_int = arr[i]
		if arr[i] < lowest_int:
			lowest_int = arr[i]
	print(lowest_int)

missing_poss(test_set_2)

