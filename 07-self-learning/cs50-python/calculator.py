# Exercise 1 (basic addition)
x = 1
y = 2

z = x + y

print(z)


# Exercise 2 (string concatenation)
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)


# Exercise 3 (type conversion)
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)


# Exercise 4 (integer addition)
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)


# Exercise 5 (float addition)
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)


# Exercise 6 (rounding)
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)


# Exercise 7 (Thousand separator)
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

# using comma as thousand separator
print(f"{z:,}")


# Exercise 8 (division)
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)


# Exercise 9 (rounding division)
x = float(input("What's x? "))
y = float(input("What's y? "))

# rounding to 2 decimal places
z = round(x / y, 2)

print(z)


# Exercise 10 (formatting division)
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

# formatting to 2 decimal places
print(f"{z:.2f}")


# Exercise 11 (formatting without trailing zeros)
def main():
    x = float(input("What's x? "))
    print("x squared is", format_square(x))


def format_square(n):
    return n * n


main()