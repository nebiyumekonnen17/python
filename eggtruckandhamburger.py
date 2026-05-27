# Eggs and flour
eggs = int(input("Enter number of eggs: "))
flour = 0

for egg in range(eggs):
    flour += 2

print("Total flour needed:", flour, "cups")


# Packages and weight
packages = int(input("\nEnter number of packages: "))
total_weight = 0

for package in range(packages):
    total_weight += 2

print("Total truck weight:", total_weight, "kg")


# Burgers and inventory
burgers_ordered = int(input("\nEnter number of burgers ordered: "))
inventory = int(input("Enter current inventory: "))

for burger in range(burgers_ordered):
    inventory -= 1

print("Burgers left in inventory:", inventory)