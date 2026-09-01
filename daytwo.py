"""
score = float(input("What is your score? "))

if score>=70:
  print("You passed the exam :)")
else:
  print("You did not pass the exam :(")

gpa=float(input("What is your GPA using the . format? "))
voulunteer_hours=int(input("How many volunteer hours have you done? "))
is_club_leader=False

if gpa>=3.5 and (voulunteer_hours>=50 or is_club_leader):
  print("You qualify for the scholarship.")
else:
  print("You do not qualify for the scholarship")

has_key=True
chest_locked= False

if has_key:
  if not chest_locked:
    print("You found the treasure!")
  else:
     print("The chest is still locked.")
else:
  print("You don't have the key")

is_student=True
age=int(input("What is your age? "))
ticket_price=0

if age<5:
  ticket_price=0
elif age <=12:
  ticket_price=8
elif age <=17:
  ticket_price=12
elif age <=64:
  ticket_price=15
else:
  ticket_price=10

if age>=18 and is_student:
  ticket_price-=3

print(f"Your ticket is ${ticket_price}")

username=input("Please enter your username: ")

if username.strip().lower()=="admin":
  password=input("Enter your password: ")

  if password=="python123":
    print("Login successful")
  else:
    print("Incorrect password")

else:
  print("Username not found")

"""

gpa=float(input("Enter your gpa: "))
completed_credits=int(input("Enter the number of completed credits: "))
has_prerequisites=True
is_suspended=False

if has_prerequisites and not is_suspended:
  if completed_credits>=30 or gpa>=3.8:
    if gpa>=3.5:
      print("Priority registration")
    elif gpa>=2.0:
      print("Standard registration")
    else:
      print("Registration denied: GPA too low")
  else:
    print("Registration denied: requirements not met")
else:
  print("Registration denied: requirements not met")

account_balance=1000.0
correct_pin="4821"
is_account_locked=False
is_verified=True

pin=input("Enter your pin: ")
if not is_account_locked:
  if pin==correct_pin:
    withdrawal_amount=float(input("How much would you like to withdraw?: "))

    if withdrawal_amount<=0:
      print("Invalid withdrawal amount.")
    elif withdrawal_amount>account_balance:
      print("Insufficient funds.")
    elif not is_verified and withdrawal_amount>500:
      print("Verification required for withdrawals over $500.")
    else:
      account_balance-=withdrawal_amount
      print("Withdrawal successful.")
      print(f"Remaining balance: ${account_balance}")
  else:
    print("Incorrect pin")

else:
  print("Account locked.")