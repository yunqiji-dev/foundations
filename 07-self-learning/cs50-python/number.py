# Example 1
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


# Example 2
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# Example 3
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

    print(f"x is {x}")


# Example 4
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()


# Example 4
def main():
    x = get_int2()
    print(f"x is {x}")


def get_int2():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()


# Example 6
def main():
    x = get_int3()
    print(f"x is {x}")


def get_int3():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")


main()


# Example 7
def main():
    x = get_int4()
    print(f"x is {x}")


def get_int4():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()


# Example 7
def main():
    x = get_int5("what's x")
    print(f"x is {x}")


def get_int5(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
