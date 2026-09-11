"""
coordinates=(40.7128, -74.0060)
items=["bananas", "apples"]
items.append("oranges")
items.remove("apples")

visitors = [
  "Alex",
  "Maria",
  "John",
  "Alex",
  "David",
  "Maria",
  "Sarah",
  "John"
]
unique_visitors =set(visitors)

print(len(unique_visitors))

morning_shift={"Alex","Maria","John","David"}
night_shift={"Maria","David","Sarah","Kevin"}

print(morning_shift|night_shift)
print(morning_shift&night_shift)
print(morning_shift-night_shift)
print(night_shift-morning_shift)

python_workshop={"Alex","Maria","John","David","Lisa"}
robotics_workshop={"Maria","David","Sarah","Kevin"}
ai_workshop={"Alex","Maria","Sarah","Kevin"}
unique_students=python_workshop|robotics_workshop|ai_workshop

print(python_workshop|robotics_workshop|ai_workshop)
print(python_workshop&robotics_workshop)
print((python_workshop&ai_workshop)-robotics_workshop)
print(ai_workshop-python_workshop-robotics_workshop)
print(unique_students)
print(len(unique_students))

coding_club = {"Alex", "Maria", "John", "David"}
music_club = {"Maria", "David", "Sarah", "Kevin"}

print(coding_club|music_club)
print(coding_club&music_club)
print(coding_club-music_club)
print(music_club-coding_club)
print(coding_club^music_club)

number = int(input("Guess a number dumbo: "))
rightNo = 17

while number!= rightNo:
  print("Try harder DUMBO")
  number = int(input("Guess another number:"))

print("Woooow, I'm surprised you got it")
"""