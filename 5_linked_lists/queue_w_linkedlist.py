# Problem: Next in Queue
# Each user on a music app should have a queue of songs to play next. Implement 
# the class Queue using a singly linked list. Recall that a queue is a First-In-First-Out (FIfO) 
# data structure where elements are added to the end (the tail) and removed from the front (the head).
# Your queue must have the following methods:
# __init()__: Initializes an empty queue (provided
# enqueue(): Accepts a tuple of two strings (song, artist) and adds the element with the specified tuple to the end of the queue.
# dequeue(): Removes and returns the element at the front of the queue. If the queue is empty, returns None.
# peek(): Returns the value of the element at the front of the queue without removing it. If the queue is empty, returns None.
# is_empty(): Returns True if the queue is empty, and False otherwise.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def enqueue(self, music):
        new_node = Node(music)

        if self.is_empty():
             self.front = new_node
        else:
            self.rear.next = new_node

        self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return None
        # save current head in temp
        temp = self.front
        # assign head.next to head
        self.front = self.front.next
        # temp.next = None
        temp.next = None
        # return temp
        return temp

    def peek(self):
        return self.front

q = Queue()
#print(q.is_empty())
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.dequeue()
print_queue(q)
