"""
account_balance=1000.0
correct_pin="4821"
is_account_locked=False
is_verified=True

def pin_verification(entered_pin, correct_pin):
  if entered_pin==correct_pin:
    return True
  return False

def withdraw(amount, account_balance, is_verified):
  if amount<=0:
    return "Invalid amount"
  elif amount>account_balance:
    return "Insufficient funds"
  elif amount>500 and not is_verified:
    return "Verification required for withdrawal over $500"
  return "Valid"
def calculate_balance(amount, account_balance):
  return account_balance-amount

if not is_account_locked:
  pin=input("Enter your pin: ")
  final_pin=pin_verification(pin,correct_pin)

  if final_pin:
    withdrawal_amount=float(input("How much do you want to withdraw?: "))
    final_amount=withdraw(withdrawal_amount, account_balance, is_verified)

    if final_amount=="Valid":
      new_balance = calculate_balance(withdrawal_amount, account_balance)
      print("Withdrawal successful")
      print(f"Remaining balance: ${new_balance}")
    else:
      print(final_amount)
  else:
    print("Incorrect pin")
else:
  print("Account locked")
"""
account_balance = 1500.0
correct_pin = "7392"
is_account_locked = False
daily_transfer_limit = 800

def check_pin(entered_pin, correct_pin):
  if entered_pin==correct_pin:
    return True
  return False
def transfer_limit(amount,daily_transfer_limit):
  if amount<=daily_transfer_limit:
    return True
  return False
def transfer_requirement(amount, account_balance, daily_transfer_limit):
  if amount<=0:
    return "Invalid amount"
  elif amount>account_balance:
    return "Insufficient funds"
  elif not transfer_limit(amount, daily_transfer_limit):
     return "Daily limit reached"
  return "Proceed"
def transfer(amount, account_balance):
    account_balance-=amount
    return account_balance

if is_account_locked:
  print("Account is locked, cannot proceed.")
else:
  pin=input("Enter your pin: ")
  e_pin=check_pin(pin, correct_pin)
  if e_pin:
    transfer_amount=float(input("How much do you want to transfer?: "))
    amount_to_transfer=transfer_requirement(transfer_amount, account_balance, daily_transfer_limit)
    if amount_to_transfer=="Proceed":
      new_amount=transfer(transfer_amount, account_balance)
      print(f"Transfer successful. Remaining balance: ${new_amount}")
    else:
      print(amount_to_transfer)
  else:
    print("Incorrect pin")
