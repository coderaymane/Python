chaine = input("Entrez une chaîne : ")
voyelles = "aeiouyAEIOUY"
compteur = sum(1 for char in chaine if char in voyelles)
print(f"La chaîne contient {compteur} voyelle(s).")
