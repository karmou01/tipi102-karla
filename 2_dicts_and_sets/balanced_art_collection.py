# Problem: Balanced Art Collection

# As the curator of an art gallery, you are organizing a new exhibition. 
# You must ensure the collection of art pieces are balanced to attract the right range of buyers. 
# A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1. 
# Given an integer array art_pieces representing the value of each art piece, 
# write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.
# A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

def find_balanced_subsequence(art_pieces):
    d = {}
    
    for i in range(len(art_pieces)):
        if art_pieces[i] not in d:
            d[art_pieces[i]] = 1
        else:
            d[art_pieces[i]] = d[art_pieces[i]] + 1

    result = 0
    for key in d:
        if key + 1 in d:
            result = max(result, d[key] + d[key+1])
    
    return result

# Tests

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]
art_pieces4 = [1,5,5,5]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces4))