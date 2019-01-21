# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
def stairClimb(N, stairsClimbed = 0):
	x += 1
	if stairsClimbed == N:
		print("Climb check reached")
		return
	if N - stairsClimbed >= 2:
		print("+2", stairsClimbed)
		stairClimb(N, stairsClimbed + 2)
	if N - stairsClimbed >= 1:
		print("+1", stairsClimbed)
		stairClimb(N, stairsClimbed + 1)
print(stairClimb(4, 0))

# solves the primary problem, doesnt count them for me.



