# Problem: Remove Duplicates

# Write a function remove_dupes() that accepts a sorted array items, and removes the
# duplicates in-place such that each element appears only once. Return the length of the modified array.
# You may not create another array; your implementation must modify the original input array items.

def remove_dupes(items):
    i = 0
    j = 1
    for i in range(len(items) - 1):
        for j in range(len(items) - 2):
            if items[i] == items[j]:
                items.remove(items[j])
            else:
                j += 1
        j = 0
        i += 1
    print(items)
    return len(items)

# Tests

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)