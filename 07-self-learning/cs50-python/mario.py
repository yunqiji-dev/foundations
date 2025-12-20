# Example 1
print("#")
print("#")
print("#")


# Example 2
for _ in range(3):
    print("#")


# Example 3
def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()


# Example 4
def main():
    print_column2(3)


def print_column2(height):
    print("#\n" * height, end="")


main()


# Example 5
def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()


# Example 6
def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")

        print()


main()


# Example 7
def main():
    print_square2(3)


def print_square2(size):
    for i in range(size):
        print("#" * size)


main()


# Example 8
def main():
    print_square3(3)


def print_square3(size):
    for i in range(size):
        print_row2(size)


def print_row2(width):
    print("#" * width)


main()
