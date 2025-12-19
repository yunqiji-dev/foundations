# Example 1
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


# Example 2
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(students[i])


# Example 3
students = ["Hermione", "Harry", "Ron", "Draco"]
house = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# Example 4
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# Example 5
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")


# Example 6
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
