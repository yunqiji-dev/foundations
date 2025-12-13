# Exercise 1 (print function)
print("hello,world")


# Exercise 2 (input function)
print("What's your name? ")
name = input()
print("hello, ")
print(name)


# Exercise 3 (commenting code)
# Ask for user's name


# Say hello to user


# Exercise 4 (string concatenation)
# Ask for user's name
name = input("What's your name? ")

# Say hello to user
print("hello, " + name)


# Exercise 5 (argument separation)
# Ask for user's name
name = input("What's your name? ")

# Say hello to user
print("hello,", name)


# Exercise 6 (end parameter)
# Ask for user's name
name = input("What's your name? ")

# Say hello to user
print("hello, ", end="")
print(name)


# Exercise 7 (sep parameter)
# Ask for user's name
name = input("What's your name? ")

# Say hello to user
print("hello", name, sep=", ")


# Exercise 8 (f-strings)
# Ask for user's name
name = input("What's your name? ")

# Say hello to user
print(f"hello, {name}")


# Exercise 9 (removing whitespace)
# Ask for user's name
name = input("What's your name? ")

# Remove whitespace from string
name = name.strip()

# Say hello to user
print(f"hello, {name}")


# Exercise 10 (capitalizing names)
# Ask for user's name
name = input("What's your name? ")

# Remove whitespace from string
name = name.strip()

# Capitalize the first letter of the name
name = name.capitalize()

# Say hello to user
print(f"hello, {name}")


# Exercise 11 (title casing names)
# Ask for user's name
name = input("What's your name? ")

# Remove whitespace from string and capitalize user's name
name = name.strip().title

# Say hello to user
print(f"hello, {name}")


# Exercise 12 (splitting names)
# Ask for user's name
name = input("What's your name? ").strip().title()

# Split the name into first and last names
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")


# Exercise 13 (defining functions)
def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)


# Exercise 14 (default parameters)
def hello(to="world"):
    print(f"hello, {to}")


hello()
name = input("What's your name? ")
hello(name)


# Exercise 15 (main function)
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print(f"hello, {to}")


main()
