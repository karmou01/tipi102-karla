# Problem: Reverse User Comments Queue
# On your platform, comments on posts are displayed in the order they are received. 
# However, for a special feature, you need to reverse the order of comments before displaying them. 
# Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
    # initialize empty list
    stack = []
    list = []
    # while stack is not empty
    for comment in comments:
        stack.append(comment)
    
    while stack:
        # enqueue last elt of stack onto list
        list.append(stack[-1])
        # pop last element
        stack.pop()
    
    return list

# Tests

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))