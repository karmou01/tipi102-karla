class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    idx = 0
    curr = playlist1
    while idx < a - 1:
          curr = curr.next
          idx += 1
    
    temp = curr
    prev = curr

    while idx < b:  # i changed it from b - 1 to b, can you try running it LOL
        prev = curr
        curr = curr.next
        prev.next = None
        idx += 1

    temp.next = playlist2
    
    ptr = playlist2
    while ptr.next != None:
        ptr = ptr.next
    
    ptr.next = curr.next 

    return playlist1

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                         Node(('Ego Death', 'The Internet')))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 1, 2))
