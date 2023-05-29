
print("Hello! Welcome to Soul Coffee!!\n\n")

name = input("What is your name? ")

menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"

order = input(f"Nice to meet you {name}! Today's menu is {menu}. What can i get for you? ")
if order == "Black Coffee".lower():
    x = 3
elif order == "Espresso".lower():
    x = 5
elif order == "Frappuccino".lower():
    x = 11
elif order == "Latte".lower() or order == "Cappuccino".lower():
    whipped_cream = input("Would you like whipped cream with that? ")
    if whipped_cream == "Yes".lower():
        x = 10
    elif whipped_cream == "No".lower():
        x = 7


quantity = int(input("No problem! How many would you like? "))
order_total = x * quantity

print(f"Gotcha! We'll have that ready for you in no time! That'll be ${order_total}, please.")