def triangle():
    i = 0
    while i <= 5:
        print("*" * i)
        i += 1

def square():
    i = 5
    ligne = 0
    while ligne <= 2:
        print("*" * i)
        ligne += 1

def rectangle():
    i = 10
    ligne = 0
    while ligne <= 2:
        print("*" * i)
        ligne += 1

while True:
    user_input = input("(T)riangle - (S)quare - (R)ectangle - '(E)exit': ").lower()
    if user_input == "e":
        break
    elif user_input == "t":
        triangle()
    elif user_input == "s":
        square()
    elif user_input == "r":
        rectangle()
    else:
        print("Invalid input, Try again!")


