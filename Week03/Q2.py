# Q2 Shopping List
cart = ["apple","banana","milk","bread","apple","eggs",]
apple_count = cart.count("apple")
print("We have", apple_count, "apples")
print("Milk postion:", cart.index("milk"))
cart.remove("apple")
print("Removed items with pop:", cart.pop())
print("Is the banana in cart?", "banana" in cart)
print("Finale cart: ", cart)