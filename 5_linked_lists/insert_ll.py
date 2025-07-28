# Problem: Selective DNA Deletion
# As a biologist, you are working on editing a long strand of DNA represented 
# as a linked list of nucleotides. Each nucleotide in the sequence is represented
#  as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.
# Given the head of the linked list dna_strand and two integers m and n, write a
# function edit_dna_sequence() that simulates the selective deletion of nucleotides
# in a DNA sequence. You will: - Start at the beginning of the DNA strand. 
# - Retain the first m nucleotides from the current position. - Remove the next n nucleotides
# from the sequence. - Repeat the process until the end of the DNA strand is reached.
# Return the head of the modified DNA sequence after removing the mentioned nucleotides.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution
#  has the stated time and space complexity.

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

def edit_dna_sequence(dna_strand, m, n):
    current = dna_strand
    while current:
        for _ in range(1, m):
            if current is None:
                return dna_strand
            current = current.next
        temp = current

        if current.next is None:
            return dna_strand
        for _ in range(n):
            if temp is None:
                return dna_strand
            temp = temp.next
        
        current.next = temp
        current = current.next

    return dna_strand
    

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))