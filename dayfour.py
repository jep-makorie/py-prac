subtotal=0
item_count=0
is_finished=False

while not is_finished:
  item_price=float(input("Enter item price(0 to checkout): "))

  if item_price==0:
    is_finished=True
  elif item_price<0:
    print("Invalid price.")
  else:
    subtotal+=item_price
    item_count+=1

while True:
  membership=input("Are you a member?(yes/no):")

  if membership.strip().lower()=="yes":
    discount=subtotal*0.10
    break
  elif membership.strip().lower()=="no":
    discount=0
    break
  else:
    print("Invalid input.")

total=subtotal-discount

print(f"Items purchased: {item_count}")
print(f"Subtotal: ${subtotal}")
print(f"Discount: ${discount}")
print(f"Total: ${total}")

"""
def show_menu():
  print("1. Check balance")
  print("2. Withdraw")
  print("3. Deposit")
show_menu()
show_menu()

def show_balance(balance):
  print(f"Your balance is ${balance}")
show_balance(1000)
show_balance(750)

def purchase(price, quantity):
  return price*quantity
total=purchase(4.50,3)
print(f"Total cost: ${total}")

def check_pin(entered_pin, correct_pin):
  if entered_pin==correct_pin:
    return "Access granted"
  return "Incorrect pin"

message=check_pin("4721","4821")
print(message)


def free_shipping(total, member):

  if total>=30 and member=="yes":
    return True
  elif total>=50 and member=="no":
    return True
  return False

total1=float(input("What is your total?: "))
membership= input("Are you a member?: ")
membership=membership.strip().lower()

if free_shipping(total1, membership):
  print(f"${total1} order. Free shipping applied")
else:
  print(f"${total1} order. Shipping fee required")
"""
def movie_checkout(price, age, student):
  if age<=11:
    return price*0.5
  elif student=="yes":
    return price*0.8
  return price

ticket_price=float(input("What is the original price of the ticket?: "))
age=int(input("How old are you?: "))
is_student=input("Are you are student?: ")
is_student=is_student.lower().strip()
final_price = movie_checkout(ticket_price, age, is_student)

print(f"Final price: ${final_price}")