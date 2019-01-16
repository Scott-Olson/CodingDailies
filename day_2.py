# 1/10/2018
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

# plan: iterate through the list once, multiply all the elements
# there is probably a function or tool for this, but manual for now
# iterate over the list again and divide by the current element


# this functions with division
def array_multi(list):
	product = list[0]
	for i in range(1,len(list)):
		product *= list[i]

	answer = []
	for i in range(0,len(list)):
		answer.append(product/list[i])

	print(answer)


array_multi([1, 2, 3, 4, 5])







