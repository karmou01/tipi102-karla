# Problem 1: Find Millenium Falcon Part
# Han Solo's ship, the Millenium Falcon, has broken down and he's searching for
# a specific replacement part. As a repair shop owner helping him out, write a 
# function check_stock() that takes in a list inventory where each element is an
# integer ID of a part you stock in your shop, and an integer part_id representing
# the integer ID of the part Han Solo is looking for. Return True if the part_id is
# in inventory and False otherwise.
# Your solution must have O(log n) time complexity.

def check_stock(inventory, part_id):
    l = 0
    r = len(inventory) - 1

    while l <= r:
        mid = (l + r) // 2

        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            l = mid + 1
        elif inventory[mid] > part_id:
            r = mid - 1
        else:
            return False
        
    return False

# Tests

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))

# Problem 2: Find Millenium Falcon Part II
# If you implemented your check_stock() function from the previous problem iteratively,
# implement it recursively. If you implemented it recursively, implement it iteratively.   

def check_stock(inventory, part_id):
    l = 0
    r = len(inventory) - 1
    mid = (l + r) // 2

    if not inventory:
        return False
    # base case: 
    if inventory[mid] == part_id:
        return True
    
    if l > r:
        return False
    elif inventory[mid] > part_id:
        return check_stock(inventory[: mid], part_id)
    elif inventory[mid] < part_id:
       return check_stock(inventory[mid + 1: ], part_id)
        
# Tests

print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100)) 