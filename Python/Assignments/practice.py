# # Age Group Categorization

# age = int(input("Please enter your age: "))

# if age < 15:
#     print("You are a child.")
# elif age < 20:
#     print("You are a teenager.")
# elif age < 30:
#     print("You are a young adult.")
# else:
#     print("You are a senior.")  



# Movie Ticket Price Calculation

# age = int(input("Please enter your age: "))
# days = input("Please enter the day of the week: ").lower()

# price = 12 if age >= 20 else 8

# price = 12

# if age >= 20: 
#     price = 12
#     print(f"You are Adult and Your Ticket Price is ${price}")
# else:
#     price = 8
#     print(f"You are Child and Your Ticket Price is ${price}")

# if days == "wednesday":
#     price -= 2

# print(f"Today is {days.capitalize()} and you get a $2 discount!")
# print(f"After discount Your Ticket Price is ${price}")


# score = int(input("Please enter your score: "))

# if score >= 101:
#     print("Grade invalid checked and try again!")
#     exit()

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(grade)            

# fruit = input("Enter Fruit Name: ").lower()
# color = input("Enter Fruit Colour (Good/Bad): ").lower()


# if fruit == fruit and color == "green":
#     print("The fruit is ripe and not ready to eat please few days wait.")
# elif fruit == fruit and color == "yellow":
#     print("The fruit is ripe and ready to eat.")
# elif fruit == fruit and color == "brown":
#     print("The fruit is overripe and not good to eat.")
# else:
#     print("Invalid input. Please enter 'Green', 'Yellow', or 'Brown'.")


# Start Numpy Library...


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)