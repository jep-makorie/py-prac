name=input("What is your name: ")
age=int(input("How old are you? "))
years=int(input("How many years into the future do you want to calculate? "))

print(f"{name}, your age in the future will be {age+years}")


customer_name=input("What is your name: ")
item_price=float(input("What is the price of one item? "))
total_items=int(input("How many items are you buying? "))

print(f"{customer_name}, your total for {total_items} items is ${item_price*total_items}")