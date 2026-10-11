# 3

# 3.1
food = ["sushi", "pad thai", "pie", "pasta", "chocolate"]
print(food[0])  # debugged by changing it from 1 to 0
print(food[-1])
food.append("burgers")
food.insert(0, "apple")
food.remove("pad thai") # debugged by changing it from 3 to "pad thai"
print(len(food))
upper_case = [foods.upper() for foods in food]
print(upper_case)

first_and_last = [food[:1], food[-1:]]

if "potato" in food:
    print("A potato!")
else:
    print("No potato!")

# 3.2

numbers = range(20)