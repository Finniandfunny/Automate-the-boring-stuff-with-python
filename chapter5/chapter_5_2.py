#topic: dictionary

# Fuction takes dictionary input and prints it with a for loop
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

# Function's first paraeter takes dictionary and second takes list
def addToInventory(inventory, addedItems):
    # loops over the list
    for i in addedItems:
        # if item not in dict add the item in keys
        if i not in inventory:
            inventory[i] = 1
        else:
            #if item is there just add the value once
            inventory[i]+=1;

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)