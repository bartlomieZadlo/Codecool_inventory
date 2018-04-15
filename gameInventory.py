# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print("\nInventory:")
    for i in inventory.keys():
        print("{} : {}".format(i, inventory[i]))
    print("\nTotal number of items:{}\n".format(sum(inventory.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for loot_element in added_items:
        if loot_element in inventory.keys():
            inventory[loot_element] += 1
        else:
            inventory[loot_element] = 1

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    inventory_list = []
    for inv_key in inventory.keys():
        inventory_list.append([inventory[inv_key], inv_key])
    longest_line_length = 0
    for inv_key in inventory.keys():
        line_length = len(inv_key) + len(str(inventory[inv_key]))
        if line_length > longest_line_length:
            longest_line_length = line_length
    longest_line_length += 10

    print("Inventory:")
    print("-" * longest_line_length)
    header_indent = longest_line_length - 16
    print(("  count{}item name".format(" " * header_indent)))
    if order is None:
        for inv_key in inventory.keys():
            line_length = len(str(inv_key)) + len(str(inventory[inv_key]))
            total_whitespace_count = longest_line_length - line_length
            first_indent = int(7 - len(str(inventory[inv_key])))
            second_indent = int(total_whitespace_count - 7 + len(str(inventory[inv_key])))
            print(("{}{}{}{}").format(
                " " * first_indent,
                inventory[inv_key],
                " " * second_indent,
                inv_key,
                ))
    elif order == "count,desc":
        inventory_list = sorted(inventory_list)
        print_rows(inventory_list)
    elif order == "count,asc":
        inventory_list = sorted(inventory_list, reverse=True)
        print_rows(inventory_list)
    print("-" * longest_line_length)
    print("Total number of items: {}".format(sum(inventory.values())))


def print_rows(inventory_tuple_list):
    for inv_element in inventory_list:
            line_length = len(str(inv_element[0])) + len(str(inv_element[1]))
            total_whitespace_count = longest_line_length - line_length
            first_indent = 7 - len(str(inv_element[0]))
            second_indent = total_whitespace_count - 7 + len(str(inv_element[0]))
            print("{}{}{}{}").format(
                " " * first_indent,
                inv_element[0],
                " " * second_indent,
                inv_element[1],
            )
# Imports new inventory items from a file
# The filename comes as an argument, but by default it"s
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    imported_items = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            imported_items.append(line.split(","))
    imported_items = imported_items[0]
    imported_items[-1] = imported_items[-1].rstrip()
    add_to_inventory(inventory, imported_items)

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
        with open(filename, 'w+', newline='') as f:
            counter = 0
            for inv_element in inventory.keys():
                for inv_value in range(0, int(inventory[inv_element])):
                    counter += 1
                    if counter == sum(inventory.values()):
                        f.write(
                            ("{}").format(inv_element)
                        )
                    else:
                        f.write(
                            ("{},").format(inv_element)
                        )


inv={
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12,
}

dragon_loot=[
    "gold coin",
    "dagger",
    "gold coin",
    "gold coin",
    "ruby",
]

import_inventory(inv)
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print_table(inv)
export_inventory(inv)
