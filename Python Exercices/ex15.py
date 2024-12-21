n = int(input("Entrez une valeur pour n : "))
somme = sum(i for i in range(2, n + 1, 2))
print(f"La somme des nombres pairs entre 1 et {n} est : {somme}")
