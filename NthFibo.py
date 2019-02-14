
# solution 1 golphed, counter method. Efficient O(n) time: O(1) space

def fibSeq(n):
	lastTwo = [0, 1]
	counter = 3

	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1 
	# not a fan of returning an if else but it cleans it up
	return lastTwo[1] if n > 1 else lastTwo[0]
	# this function passed all tests, could be an edge case thats missed

# solution 2 golphed, recursion. O(2^n) time: O(n) space
def getNthFib(n):
	if n == 2:
		return 1
	elif n == 1:
		return 0
	return getNthFib(n - 1) + getNthFib(n - 2)
	# fully functional on all tests