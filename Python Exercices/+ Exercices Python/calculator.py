# Simple Calculator by @coderaymane

# --- functions ---

def additon():
    print("Result: ", float(x) + float(y))

def subtraction():
        print("Result: ", float(x) - float(y))

def multiplication():
        print("Result: ", float(x) * float(y))

def division():
        print("Result: ", float(x) / float(y))
     
# --- calculator ---

while True:
    print("Enter the first number:")
    x = input("> ")
    if x.lower() == "quit":
        break
    print("Enter the operator (+,-,*,/)")
    opr = input("> ")
    print("Enter the second number:")
    y = input("> ")
    if opr == "+":
        additon()
    elif opr == "-":
        subtraction()
    elif opr == "*":
        multiplication()
    elif opr == "/":
        division()
    else:
        print("Invalid inputs, Pls try again or type 'quit' to exit!")

