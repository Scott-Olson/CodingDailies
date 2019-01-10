# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# iterate over the list looking at the a previous number that would sum to the k value

def list_sum(list, k):
	previous = {}
	for i in range(0,len(list)):
		remainder = k - list[i]
		if remainder in previous:
			print("Found match: ", list[i], remainder)
			return True
		else:
			print("not found, adding to the list: ", list[i])
			previous[list[i]] = 1


print(list_sum([10,15,3,5,6,6,25,5,-8,3,5,5,2,2,5,4,4,8,9,8,2,6,7,9,9,0,0,9,8,8], 17))