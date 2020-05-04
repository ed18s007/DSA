class Node(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

class LinkedList:
	def __init__(self, init_list=None):
		self.head = None
		if init_list is not None:
			for value in init_list:
				self.append(value)

	def append(self, value):
		if self.head is None:
			self.head = Node(value)
			return
		else:
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = Node(value)
			return

def iscircular(linked_list):
    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next
        
        if slow == fast:
            return True

# Test Cases
list_with_loop = LinkedList([2, -1, 3, 0, 5])
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
	node = node.next   
node.next = loop_start

# print(list_with_loop.head.value)
# print(type(list_with_loop))
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head
print ("Pass" if iscircular(list_with_loop) else "Fail")
print ("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
print ("Pass" if not iscircular(LinkedList([1])) else "Fail")
print ("Pass" if iscircular(small_loop) else "Fail")
print ("Pass" if not iscircular(LinkedList([])) else "Fail")

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.value, end =" ")
			temp = temp.next

	def detectLoop(self):
		s = set()
		temp = self.head
		while(temp):
			if (temp in s):
				return True
			s.add(temp)
			temp = temp.next
		return False

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

if (llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop")

llist.head.next.next.next.next = llist.head; 
if (llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop")

llist = LinkedList()
llist.push(0)
llist.head.next = llist.head

if (llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop")

llist = LinkedList()
if (llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop")