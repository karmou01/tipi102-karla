# Problem: Post Format Validator
# You are managing a social media platform and need to ensure that posts are properly formatted. 
# Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
# You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

# A post is considered valid if:
# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.

# def is_valid_post_format(posts):
#     #create stack and a map for each variable 
#     #for statememt to check each char 
#     #append each char 
#     stack = []
#     detailed_map = {')': '(',
#                     '}' : '{',
#                     ']' : '[',
#                     }
#     for char in posts:
#         if char in detailed_map.values(): # If char is in the map
#             stack.append(char) # Add it to the stack
#         elif char in detailed_map: # If the character is a closing character
#                 # pop only if the two parathesis match, cause not every closing 
#                 # paranthesis necessarily means that we need to pop
#                 if stack and stack[-1] == char:
#                     stack.pop()
                    
#     return len(stack) == 0 # return the status of the stack, cleaner + to avoid redundancy
 

    
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))