# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time


def schedule(f, n):
	milli = n/1000
	time.wait(milli)
	f()