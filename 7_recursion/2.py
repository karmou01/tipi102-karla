# Problem: Counting Iron Man's Suits
# Tony Stark, aka Iron Man, has designed many different suits over the years. 
# Given a list of strings suits where each string is a suit in Stark's collection, 
# count the total number of suits in the list. Implement the solution iteratively
# without the use of the len() function. Implement the solution recursively. 
# Discuss: what are the similarities between the two solutions? What are the differences?

def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    # base case
    if len(suits) == 0: # suit list is equal to 1
        return 0
    if len(suits) == 1: # suit list is equal to 1
        return 1

    else:
    # recursive case
        return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
