# 1/11/2018
# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# not sure I totally understand this one, should look into it more

def serialize(tree):
	# traverse tree, convert to string
	ser_tree = ""



	return ser_tree


def deserialize():
	# pattern is to watch for 1, 2, 4, 8, 16, ... in string format

serialize()
deserialize()