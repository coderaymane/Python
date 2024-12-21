n = int(input("Entrez un nombre : "))
factorielle = 1
i = 1
while i <= n:
    factorielle *= i
    i += 1
print(f"La factorielle de {n} est : {factorielle}")
