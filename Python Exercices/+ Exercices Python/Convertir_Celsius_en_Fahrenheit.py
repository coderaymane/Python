température = input("La température: ")
Choose_C_or_F = input("(C)elsius or (F)ahrenheit: ")

if Choose_C_or_F.upper() == "C":
    print("La température en Fahrenheit: ", float(température) * 9 / 5 + 32 )
elif Choose_C_or_F.upper() == "F":
    print("La température en Celsius",(float(température)-32) * 5 / 9)
else:
    print("Invalid inputs, Pls try again!")