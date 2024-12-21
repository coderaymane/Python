n = int(input("Entrez une valeur pour n : "))
print("Nombres impairs entre 1 et", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
