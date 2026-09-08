"""
book= {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "pages": 310,
  "available": True
}
print(f'{book["title"]} has {book["pages"]} pages.')
print(f'Available: {book["available"]}')

profile= {
  "username": "skywalker22",
  "followers": 125,
  "posts": 17
}

profile["followers"]+=8
profile["posts"]+=1
profile["verified"]=False

print(profile)

settings= {
  "theme":"dark",
  "notifications": True,
  "language": "English"
}

if "notifications" in settings:
  print(settings["notifications"])
if "location" in settings:
  print(settings["location"])
else:
  print("Location not set.")

weather= {
  "city": "New York",
  "temperature": 72,
  "condition": "Sunny"
}
temperature=weather.get("temperature")
humidity=weather.get("humidity", 0)

print(f"Temperature: {temperature}")
print(f"Humidity: {humidity}")

inventory = {
    "keyboard": 6,
    "mouse": 0,
    "monitor": 3,
    "webcam": 8,
    "headphones": 0
}

for product in inventory:
  if inventory[product]>0:
    print(f'{product}: {inventory[product]} in stock.')

for product, quantity in inventory.items():
  if quantity > 0:
    print(f"{product}: {quantity} in stock.")

grades= {
  "Essay": 88,
  "Midterm": 73,
  "Project": 94,
  "Quiz": 67,
  "Final": 91
}

for assignment, grade in grades.items():
  if grade>=80:
    print(f'{assignment}: {grade}')

courses = [
    {
        "name": "Calculus",
        "credits": 4,
        "completed": True
    },
    {
        "name": "Physics",
        "credits": 4,
        "completed": False
    },
    {
        "name": "Python",
        "credits": 3,
        "completed": True
    },
    {
        "name": "Chemistry",
        "credits": 4,
        "completed": False
    }
]

for course in courses:
  if course["completed"]:
    print(f'{course["name"]}: {course["credits"]} credits')

student = {
  "name": "Jordan",
  "grade": 84,
  "attendance": 92
}
def is_passing(student):
  if student["grade"]>=70 and student["attendance"]>=80:
    return True
  return False

status=is_passing(student)
print(status)

def create_movie(title,year,rating):
  return {
    "title": title,
    "year": year,
    "rating": rating
  }
movie=create_movie("Inception",2010,8.8)
print(movie)

def count_low_battery(devices):
  count=0
  for device in devices:
    if device["battery"]<20:
      count+=1
  return count

devices = [
    {
        "name": "Laptop",
        "battery": 73
    },
    {
        "name": "Phone",
        "battery": 18
    },
    {
        "name": "Tablet",
        "battery": 42
    },
    {
        "name": "Headphones",
        "battery": 9
    }
]
low_devices=count_low_battery(devices)
print(low_devices)

def get_pending_orders(orders):
  pending_customers=[]
  for order in orders:
    if not order["shipped"]:
      name=order["customer"]
      pending_customers.append(name)
  return pending_customers

orders = [
    {
        "customer": "Maya",
        "total": 85,
        "shipped": True
    },
    {
        "customer": "Alex",
        "total": 42,
        "shipped": False
    },
    {
        "customer": "Jordan",
        "total": 120,
        "shipped": True
    },
    {
        "customer": "Sam",
        "total": 65,
        "shipped": False
    }
]
pending=get_pending_orders(orders)
print(pending)


def analyze_inventory(products):
  no_stock=0
  available_products=0
  total_units=0
  for product in products:
    if product["quantity"]==0:
     no_stock+=1
    else:
      available_products+=1
      total_units+=product["quantity"]
  
  return {
    "available_products": available_products,
    "out_of_stock": no_stock,
    "total_units": total_units
  }
products = [
    {"name": "Keyboard", "price": 45, "quantity": 6},
    {"name": "Mouse", "price": 20, "quantity": 0},
    {"name": "Monitor", "price": 180, "quantity": 3},
    {"name": "Webcam", "price": 35, "quantity": 8}
]
stock=analyze_inventory(products)
print(stock)

def create_report(students):
  passing_count=[]
  failing_count=[]
  total_grades=0
  highest_grade=0
  #highest_grade=max(student["grade"] for student in students)
  for student in students:
    if student["grade"] > highest_grade:
      highest_grade = student["grade"]
    if student["grade"]>=70 and student["attendance"]>=80:
      name=student["name"]
      passing_count.append(name)
    else:
      name=student["name"]
      failing_count.append(name)

    total_grades+=student["grade"]
    
  average=total_grades/len(students)

  return {
    "passing_students": passing_count,
    "failing_students": failing_count,
    "highest_grade": highest_grade,
    "average_grade": average
  }
students = [
    {"name": "Aisha", "grade": 85, "attendance": 92},
    {"name": "Brian", "grade": 64, "attendance": 88},
    {"name": "Carlos", "grade": 91, "attendance": 76},
    {"name": "Diana", "grade": 72, "attendance": 95}
]

report=create_report(students)
print(report)
"""
def analyze_orders(orders):
  completed_customers=[]
  pending_customers=[]
  completed_items=0
  completed_revenue=0
  largest_completed_order=0
  for order in orders:
    if order["status"]=="completed":
      name=order["customer"]
      completed_items+=order["quantity"]
      total_revenue=order["price"]*order["quantity"]
      completed_revenue+=total_revenue
      completed_customers.append(name)
      if total_revenue>largest_completed_order:
        largest_completed_order=total_revenue
    elif order["status"]=="pending":
      name=order["customer"]
      pending_customers.append(name)
  return {
    "completed_customers": completed_customers,
    "pending_customers": pending_customers,
    "completed_items": completed_items,
    "completed_revenue": completed_revenue,
    "largest_completed_order": largest_completed_order
  }

orders = [
    {"customer": "Maya", "item": "Notebook", "quantity": 3, "price": 8, "status": "completed"},
    {"customer": "James", "item": "Backpack", "quantity": 1, "price": 45, "status": "pending"},
    {"customer": "Lena", "item": "Pens", "quantity": 5, "price": 3, "status": "completed"},
    {"customer": "Noah", "item": "Calculator", "quantity": 2, "price": 25, "status": "completed"},
    {"customer": "Sara", "item": "Folder", "quantity": 4, "price": 5, "status": "pending"}
]

order_tracking=analyze_orders(orders)
print(order_tracking)
