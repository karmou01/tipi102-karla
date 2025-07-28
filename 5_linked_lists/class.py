# Problem: New Horizons
# Step 1: Copy the following code into your IDE.
# Step 2: Instantiate an instance of the class Villager, which represents characters
# in Animal Crossing. Store the instance in a variable named apollo.
# The Villager object created should have the name "Apollo", the species "Eagle",
# and the catchphrase "pah".

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# Instantiate your villager here
villager_1 = Villager("Apollo", "Eagle", "pah")
print(villager_1.catchphrase)

# Problem: Greet Player
# Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:
# Step 2: Create a second instance of Villager in a variable named bones.
# The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
bones = Villager("Bones", "Dog", "yip yap")
# Step 3: Call the method greet_player() with your name and print out "Bones: Hey there,
# <your name>! How's it going, yip yip!". For example, if your name is Tram, 
# "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

print(bones.greet_player("Yaw"))

# Problem: Update Catchphrase
# In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.
# Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".
bones.catchphrase = "ruff it up"
print(bones.greet_player("Yaw"))

# Problem: Set Character
# In the previous exercise, we accessed and modified a player’s catchphrase attribute directly.
# Instead of allowing users to update their player directly, 
# it is common to create setter methods that users can call to update class attributes. 
# This has a few different benefits, including allowing us to validate data before updating our class instance.

# Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.
# If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
# Otherwise, it should print out "Invalid catchphrase".
# Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        for char in new_catchphrase:
            if not char.isalpha() and not char.isspace():
                print("Invalid catchphrase")
                return
        
        print("Catchphrase Updated!")
        self.catchphrase = new_catchphrase

    def add_item(self, item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid:
            self.furniture.append(item_name)
            
# Tests     

alice = Villager("Alice", "Koala", "guvnor")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

# Problem: Add Furniture
# Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.
# Update the Villager class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.
# If the item is valid, add item_name to the player’s furniture attribute.
# The method does not need to return any values.
# item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".
            
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

[]
["acoustic guitar"]
["acoustic guitar", "cacao tree"]
["acoustic guitar", "cacao tree"]

# Problem 9: Nook's Cranny
# A linked list is a new data type that, similar to a normal list or array, 
# allows us to store pieces of data sequentially. The difference between a 
# linked list and a normal list lies in how each element is stored in a computer’s memory.
# In a normal list, individual elements of the list are stored in adjacent 
# memory locations according to the order they appear in the list. 
# If we know where the first element of the list is stored, it’s really easy to 
# find any other element in the list.
# In a linked list, the individual elements called nodes are not stored in sequential
#  memory locations. Each node may be stored in an unrelated memory location. 
# To connect nodes together into a sequential list, each node stores a reference or 
# pointer to the next node in the list.
# Using the provided Node class below, create a linked list Tom Nook -> Tommy 
# where the instance tom_nook has value "Tom Nook" which points to the instance tommy that has value "Tommy".

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    

tommy = Node("Tommy", None)
tom_nook = Node("Tom Nook", tommy)

# Tests

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
print(tom_nook.value) 
print(tom_nook.next.value) 
print(tommy.value) 
print(tommy.next) 
