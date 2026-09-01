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
"""

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
