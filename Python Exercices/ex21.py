nombre = input("Entrez un nombre : ")
somme = sum(int(chiffre) for chiffre in nombre if int(chiffre) % 2 != 0)
print(f"La somme des chiffres impairs est : {somme}")
