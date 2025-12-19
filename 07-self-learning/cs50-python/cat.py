# Example 1
print("Meow")
print("Meow")
print("Meow")


# Example 2
i = 3
while i != 0:
    print("Meow")
    i = i - 1


# Example 3
i = 1
while i <= 3:
    print("Meow")
    i = i + 1

# Example 4
i = 0
while i < 3:
    print("Meow")
    i += 1


# Example 5
for i in [0, 1, 2]:
    print("Meow")


# Example 5
for i in range(3):
    print("Meow")


# Example 6
for _ in range(3):
    print("Meow")


# Example 7
print("Meow\n" * 3, end="")


# Example 8
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break


# Example 9
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")


# Example 10
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("Meow")


main()
