# Problem: Blueprint Approval Process
# You are in charge of overseeing the blueprint approval process for various 
# architectural designs. Each blueprint has a specific complexity level, 
# represented by an integer. Due to the complex nature of the designs, the approval process follows a strict order:

# Blueprints with lower complexity should be reviewed first.
# If a blueprint with higher complexity is submitted, it must wait until all 
# simpler blueprints have been approved.
# Your task is to simulate the blueprint approval process using a queue. 
# You will receive a list of blueprints, each represented by their complexity level
#  in the order they are submitted. Process the blueprints such that the simpler designs (lower numbers)
#  are approved before more complex ones.

# Return the order in which the blueprints are approved.

from collections import deque

def blueprint_approval(blueprints):
    queue = deque()
    stack = [] 
    for bluey in blueprints:
        while queue and queue[0] < bluey:
            stack.append(queue.popleft())
        queue.appendleft(bluey)
        while stack:
            queue.appendleft(stack.pop())
    return queue

# Tests
print(blueprint_approval([3, 5, 2, 1, 4])) #[1, 2, 3, 4, 5]
print(blueprint_approval([7, 4, 6, 2, 5])) #[2, 4, 5, 6, 7] 
