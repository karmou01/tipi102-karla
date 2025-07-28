# Problem 3: Counting Unique Suits
# Some of Iron Man's suits are duplicates. Given a list of strings suits where 
# each string is a suit in Stark's collection, count the total number of unique suits in the list.
# Implement the solution iteratively. Implement the solution recursively.
# Discuss: what are the similarities between the two solutions? What are the differences?
# Evaluate the time complexity of each solution. Are they the same? Define your 
# variables and provide a rationale for why you believe your solution has the stated time complexity.
def count_suits_iterative(suits):
    suit_set = set(suits)
    count = 0
    for suit in suit_set:
        count += 1
    return count

def count_suits_recursive(suits):
    suit_set = set(suits)
    # base case
    if len(suit_set) == 0: # suit list is equal to 1
        return 0
    if len(suit_set) == 1: # suit list is equal to 1
        return 1

    else:
    # recursive case
        suit_set_list = list(suit_set)
        return 1 + count_suits_recursive(suit_set_list[1:])
    
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

def count_suits_recursive(suits, idx=0, seen=None):
    """
    Tail‑recursive version that never rebuilds the set or slices the list.
    Extra space: Θ(u) for `seen` + Θ(n) call‑stack frames ❶
    Time: Θ(n)
    """
    if seen is None:
        seen = set()

    if idx == len(suits):          # base case
        return len(seen)

    seen.add(suits[idx])           # visit one element
    return count_suits_recursive(suits, idx + 1, seen)