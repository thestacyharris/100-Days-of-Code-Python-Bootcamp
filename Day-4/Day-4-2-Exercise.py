# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Get total number of names in list
import random
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
bill_pay = names[random_choice]
print(bill_pay + " is going to buy the meal today.")
