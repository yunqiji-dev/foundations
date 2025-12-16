# Example 1
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# Example 2
def main():
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()


# Example 3
def main():
    if is_even2(x):
        print("Even")
    else:
        print("Odd")


def is_even2(n):
    return True if n % 2 == 0 else False


main()


# Example 4
def main():
    if is_even3(x):
        print("Even")
    else:
        print("Odd")


def is_even3(n):
    return n % 2 == 0


main()
