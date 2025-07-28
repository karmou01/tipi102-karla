# Problem: Collecting Infinity Stones
# Thanos is collecting Infinity Stones. Given an array of integers stones 
# representing the power of each stone, return the total power using a recursive approach.
# Evaluate the time complexity of your solution. Define your variables and provide
# a rationale for why you believe your solution has the stated time complexity.

def sum_stones(stones):
    if len(stones) == 0: # suit list is equal to 1
        return 0
    if len(stones) == 1: # suit list is equal to 1
        return stones[0]

    else:
    # recursive case
        return  stones[0] + sum_stones(stones[1:])
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
