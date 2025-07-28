from collections import deque 
class TreeNode:
    def __init__(self, val, key, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

# You are going to a plant swap where you can exchange cuttings of your plants for
#  new plants from other plant enthusiasts. You want to bring a mix of cuttings from
#  both common and rare plants in your collection. You track your plant collection in a binary search tree (BST)
#  where each node has a key and a val. The val contains the plant name, and the key is an integer representing the plant's rarity. 
#  Plants are organized in the BST by their key.
# To help choose which plants to bring, write a function sort_plants() which takes 
# in the BST root collection and returns an array of plant nodes as tuples in the form (key, val)
#  sorted from least to most rare. Sorted order can be achieved by performing an inorder traversal of the BST.
# Evaluate the time and space complexity of your function. Define your variables and provide
# a rationale for why you believe your solution has the stated time and space complexity. 
# Assume the input tree is balanced when calculating time and space complexity.

def sort_plants(collection):
    # base case:
    plant_list = []
    def helper(collection):
        
        if collection is None:
            return []
        
        helper(collection.left) # This returns a list
        plant_list.append((collection.key, collection.val))
        helper(collection.right) # This also returns a list
        return plant_list
    return helper(collection)

# Test case
"""""""""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)
print(sort_plants(collection))

# Problem: Flower Finding
# You are looking to buy a new flower plant for your garden. 
# The nursery you visit stores its inventory in a binary search tree (BST) where each
#  node represents a plant in the store. The plants are organized according to their names (vals)
# in alphabetical order in the BST.
# Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden and False otherwise.
# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

def find_flower(inventory, name):
    curr = inventory
    if curr is None:
        return False
    if curr.val == name:
        print(curr.val)
        return True
    elif curr.val > name:
        return find_flower(curr.left, name)
    elif curr.val < name:
        return find_flower(curr.right, name)


# Test:
"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  M  Violet
"""

values = ["Rose", "Lily", "Tulip", "Daisy", "Merrigold", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Merrigold"))  
print(find_flower(garden, "Sunflower")) 
    
