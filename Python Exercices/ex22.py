nombre = input("Entrez un nombre : ")
produit = 1
for chiffre in nombre:
    produit *= int(chiffre)
print(f"Le produit des chiffres de {nombre} est : {produit}")
