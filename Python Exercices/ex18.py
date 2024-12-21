base = int(input("Entrez la base : "))
exposant = int(input("Entrez l'exposant : "))
resultat = 1

for _ in range(exposant):
    resultat *= base

print(f"{base} élevé à la puissance {exposant} est : {resultat}")
