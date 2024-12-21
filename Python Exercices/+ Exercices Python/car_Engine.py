command = ""
while True:
    command = input("> ").lower()
    
    if command == "start":
        print("Car started...Ready!")
    elif command == "stop":
        print("Car stoped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit          
""")
    elif command == "quit":
        break
    else:
        print("I don't undersatand that!")