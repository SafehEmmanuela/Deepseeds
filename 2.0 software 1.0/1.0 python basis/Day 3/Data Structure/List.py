shopping_cart=["Apple","Bread", "Milk", "Eggs"]
numbers=[1,2,3,4,5]
mixed_items=["Alice",25, "True", 3.14]
empty_cart= []

print(f"Shopping cart: {shopping_cart}")
print(f"Numbers: {numbers}")
print(f"mixed items: {mixed_items}")
print(f"Empty cart: {empty_cart}")

# Accessing items from a list
print(f"First item: {shopping_cart[0]}")
print(f"Second item: {shopping_cart[1]}")

# getting portions 
print(f"Frist 3 items: {shopping_cart[0:3]}")

# modifying lits
shopping_cart.append("Safeh")
print(f"After adding my name: {shopping_cart}")

# adding multiple values at once
shopping_cart.extend(["Molly","Manjoah","Emma","Eleine"])
print(f"After adding the multiple items: {shopping_cart}")

# to insert
shopping_cart.insert(1, "Yogurt")
print(f"{shopping_cart}")

# to remove
shopping_cart.remove("Bread")
print(f"after removing: {shopping_cart}")

# to remove and display what you've removed and pop removes the last item on the list
remove_item= shopping_cart.pop(1)
print(f"{remove_item}")




# List Methods and operations