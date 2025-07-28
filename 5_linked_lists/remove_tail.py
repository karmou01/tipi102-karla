# Problem: Remove Tail
# The following code incorrectly implements the function remove_tail(). 
# When correctly implemented, remove_tail() accepts the head of a singly linked
# list and removes the last node (the tail) in the list. The function should
#  return the head of the modified list. Step 1: Copy this code into Replit. 
# Step 2: Create your own test cases to run the code against. Use print statements,
# print_linked_list(), and the stack trace to identify and fix any bugs so that 
# the function correctly removes the last node from the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    # 1 -> 2 -> 3 -> 4
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

# Tests:
head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head)) # Expected output: Isabelle -> Alfonso

