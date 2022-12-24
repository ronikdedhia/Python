import ctypes
class Node:
	
	def __init__(self, data):
		
		self.data = data
		
		# XOR of next and previous node
		self.npx = 0

class XorLinkedList:
	
	def __init__(self):
		
		self.head = None
		self.__nodes = []
		
	# Returns XORed value of the node addresses
	def XOR(self, a, b):
		
		return a ^ b
	
	# Insert a node at the beginning of the
	# XORed linked list and makes the newly
	# inserted node as head
	def insert(self, data):
		
		# New node
		node = Node(data)

		# Since new node is being inserted at
		# the beginning, npx of new node will
		# always be XOR of current head and NULL
		node.npx = id(self.head)

		# If linked list is not empty, then
		# npx of current head node will be
		# XOR of new node and node next to
		# current head
		if self.head is not None:
			
			# head.npx is XOR of None and next.
			# So if we do XOR of it with None,
			# we get next
			self.head.npx = self.XOR(id(node),
									self.head.npx)

		self.__nodes.append(node)
		
		# Change head
		self.head = node

	# Prints contents of doubly linked
	# list in forward direction
	def printList(self):
	
		if self.head != None:
			prev_id = 0
			curr = self.head
			next_id = 1
			
			print("Following are the nodes "
				"of Linked List:")
			
			while curr is not None:
				
				# Print current node
				print(curr.data, end = ' ')
				
				# Get address of next node: curr.npx is
				# next^prev, so curr.npx^prev will be
				# next^prev^prev which is next
				next_id = self.XOR(prev_id, curr.npx)
				
				# Update prev and curr for next iteration
				prev_id = id(curr)
				curr = self.__type_cast(next_id)

	# Method to return a new instance of type
	# which points to the same memory block.
	def __type_cast(self, id):
		
		return ctypes.cast(id, ctypes.py_object).value

if __name__ == '__main__':
	
	obj = XorLinkedList()
	
	# Create following Doubly Linked List
	# head-->40<-->30<-->20<-->10
	obj.insert(10)
	obj.insert(20)
	obj.insert(30)
	obj.insert(40)

	# Print the created list
	obj.printList()