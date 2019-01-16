# given a sorted list, find if two numbers add to a target

# my solution, passes all unit tests
def twoNumberSumSolution(array, targetSum):
    # Write your code here.
	previous = {}
	for i in range(0,len(array)):
		remainder = targetSum - array[i]
		if remainder in previous:
			print("Found match: ", array[i], remainder)
			if remainder > array[i]:
				return [array[i], remainder]
			else:
				return [remainder, array[i]]
		else:
			print("not found, adding to the array: ", array[i])
			previous[array[i]] = 1
		if i == len(array) - 1:
			return []

# algos solution
# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
	nums = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return sorted([potentialMatch, num])
		else:
			nums[num] = True
	return []



