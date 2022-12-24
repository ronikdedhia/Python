maxElements = 4
class Node:
	
	def __init__(self):	
		self.numElements = 0
		self.array = [0 for i in range(maxElements)]
		self.next = None

def printUnrolledList(n):

	while (n != None):

		# Print elements in current node
		for i in range(n.numElements):
			print(n.array[i], end = ' ')

		# Move to next node
		n = n.next

if __name__=='__main__':
	
	head = None
	second = None
	third = None

	# Allocate 3 Nodes
	head = Node()
	second = Node()
	third = Node()

	# Let us put some values in second
	# node (Number of values must be
	# less than or equal to
	# maxElement)
	head.numElements = 3
	head.array[0] = 1
	head.array[1] = 2
	head.array[2] = 3

	# Link first Node with the second Node
	head.next = second

	# Let us put some values in second node
	# (Number of values must be less than
	# or equal to maxElement)
	second.numElements = 3
	second.array[0] = 4
	second.array[1] = 5
	second.array[2] = 6

	second.next = third
	third.numElements = 3
	third.array[0] = 7
	third.array[1] = 8
	third.array[2] = 9
	third.next = None
	printUnrolledList(head)
	