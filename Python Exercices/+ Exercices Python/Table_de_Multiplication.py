nombre = int(input("Veuillez entrer un nombre : "))

print(f"Table de multiplication de {nombre} :")
for x in range(1, 11):
    resultat = nombre * x
    print(f"{nombre} x {x} = {resultat}")