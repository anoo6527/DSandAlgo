#Node class
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

#Linked List class
class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	#adding node at the front
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	#adding node at the end
	def append(self, new_data):
		new_node = Node(new_data)

		#check if list is empty
		if(self.head == None):
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next

		last.next = new_node

	#adding node at a given position
	def insert_node(self, prev_node, new_data):
		new_node = Node(new_data)

		new_node.next = prev_node.next
		prev_node.next = new_node




if __name__ == '__main__':
	
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third

	llist.push(0)
	llist.append(5)
	llist.insert_node(second.next, 4)

	llist.printList()