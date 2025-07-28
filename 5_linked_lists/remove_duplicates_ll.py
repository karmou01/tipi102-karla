# Problem: Delete Duplicates in a Linked List
# Given the head of a sorted linked list, delete all elements that occur more 
# than once in the list (not just the duplicates). The resulting list should maintain 
# sorted order. Return the head of the linked list. Evaluate the time and space 
# complexity of your solution. Define your variables and provide a rationale for 
# why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    current = head
    prev = head
    while current:
        if current.next and current.value == current.next.value:
            prev.next = current.next.next
        prev = current
        current = current.next
    return head

# Tests:

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))