nombre = input("Entrez un nombre : ")
max_chiffre = max(int(chiffre) for chiffre in nombre)
print(f"Le plus grand chiffre dans {nombre} est : {max_chiffre}")
