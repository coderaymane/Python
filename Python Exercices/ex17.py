a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))

while b != 0:
    a, b = b, a % b

print(f"Le PGCD des deux nombres est : {a}")
