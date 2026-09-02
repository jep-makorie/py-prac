"""
total=0

for number in range(1, 21):
  if number%3==0:
    total+=number
print("Total:",total)

count=0
total=0

for entered in range(5):
  numbers=int(input("Enter a number: "))
  total+=numbers

  if numbers>0:
    count+=1
print("Total: ", total)
print("Positive numbers: ", count)

total=0
count_positive=0
count_negative=0

while True:
  number=int(input("Enter a number(0 to stop): "))
  if number==0:
    break
  
  total+=number

  if number>0:
    count_positive+=1
  if number<0:
    count_negative+=1
print("Total: ", total)
print("Positive numbers: ", count_positive)
print("Negative numbers: ", count_negative)

secret_number=7
count=0

while True:
  number=int(input("Guess the number: "))
  count+=1

  if number==secret_number:
    print("Correct!")
    break
  if number>secret_number:
    print("Too high")
  else:
    print("Too low")
print("Number of attempts: ", count)


sum_of_even=0
count_of_odd=0

for number in range(6):
  entered_number=int(input("Enter a number: "))

  if entered_number%2==0:
    sum_of_even+=entered_number
  else:
    count_of_odd+=1
print("Even total:", sum_of_even)
print("Odd count: ", count_of_odd)
"""

balance=1000.0
correct_pin="4821"
attempt=0
is_loggedin=False

while attempt<3 :
  pin=input("Enter your pin: ")
  attempt+=1

  if pin==correct_pin:
    is_loggedin=True
    print("Access granted.")
    break
  else:
    print("Incorrect pin")

if not is_loggedin:
  print("Account locked")

else:
  while True:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option=input("Choose an option:")

    if option=="1":
      print(f"Balance: ${balance}")
    elif option=="2":
      deposit_amount=float(input("How much do you want to deposit? "))

      if deposit_amount>0:
        balance+=deposit_amount
        print(f"New balance: ${balance}")
      else:
        print("Invalid amount")
    elif option=="3":
      withdraw_amount=float(input("How much do you want to withdraw? "))

      if withdraw_amount<=0:
        print("Invalid amount")
      elif withdraw_amount>balance:
        print("Insufficient funds")
      else:
        balance-=withdraw_amount
        print(f"New balance: ${balance}")
    elif option=="4":
      print("Goodbye!")
      break
    else:
      print("Invalid option.")
