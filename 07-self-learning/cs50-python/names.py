# Example 1
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(f"Hello, {name}")


# Example 2
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()


# Example 3
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# Example 4
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# Example 5
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())


# Example 6
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())


# Example 7
name = []

with open("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

for name in sorted(names):
    print(f"Hello,{name}")


# Example 8
with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())


# Example 9
name = []

with open("names.txt") as file:
    for line in file:
        name.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello,{name}")
