# Problem: Up and Down

# Write a function up_and_down() that accepts a list of integers lst as a 
# parameter. The function should return the number of odd numbers minus the 
# number of even numbers in the list.

def up_and_down(lst):
    odds = []
    evens = []
    for i in lst:
        if i % 2 == 1:
            odds.append(i)
        else:
            evens.append(i)
    return (len(odds) - len(evens))

# Tests

lst1 = [1, 2, 3]
test1 = up_and_down(lst1)
print(test1)

lst2 = [1, 3, 5]
test2 = up_and_down(lst2)
print(test2)

lst3 = [2, 4, 10, 2]
test3 = up_and_down(lst3)
print(test3)

