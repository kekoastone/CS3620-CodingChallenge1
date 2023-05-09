# Create a list of your favorite food items, the list should have a minimum of 5 elements.
# List out the 3rd element in the list.
# Add additional items to the current list and display the list.
# Insert an element named tacos at the 3rd index of the list and print out the list elements.

foodList = ["fruit", "pie", "pizza", "tacos", "burritos"]
print("3rd element in the list: " + foodList[2])
foodList.append("hot dogs")
foodList.append("hamburgers")
print(foodList)
foodList.insert(2, "curry")
print(foodList)


