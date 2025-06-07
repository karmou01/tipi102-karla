# Problem: Odds
# Write a function get_odds() that takes in a list of integers nums and returns 
# a new list containing all the odd numbers in nums.

def get_odds(nums):
    odds = []
    for num in nums:
        if num % 2 == 1:
            odds.append(num)
    return odds

test = [1, 2, 3, 4]
result = get_odds(test)
print(result)

# A more compact version using list comprehension would be:
# [num         for num in nums      if num % 2 == 1]
# ^ value     ^ loop               ^ condition