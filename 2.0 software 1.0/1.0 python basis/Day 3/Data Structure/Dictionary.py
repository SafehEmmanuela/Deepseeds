# Using our student dictionary
student = {
    "name": "Alice Johnson",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Calculus", "Physics"]
}

# Accessing values by key
print(f"Student name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Major: {student['major']}")

# Safer way to access values (won't crash if key doesn't exist)
print(f"GPA: {student.get('gpa', 'Not available')}")
print(f"Graduation year: {student.get('grad_year', 'Not specified')}")

# Checking if a key exists
if "courses" in student:
    print(f"Current courses: {student['courses']}")

# Getting all keys and values
print(f"All keys: {list(student.keys())}")
print(f"All values: {list(student.values())}")