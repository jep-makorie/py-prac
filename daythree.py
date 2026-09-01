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
"""

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
