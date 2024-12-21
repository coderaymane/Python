nombre_1 = int(input("Entrer le premier nombre: "))
nombre_2 = int(input("Entrer le deuxième nombre: "))
nombre_3 = int(input("Entrer le troisième nombre: "))

if nombre_1 < nombre_2 and nombre_3:
    print(nombre_1, "est le plus petit nombre")
elif nombre_2 < nombre_1 and nombre_3:
    print(nombre_2, "est le plus petit nombre")
elif nombre_3 < nombre_1 and nombre_2:
    print(nombre_3, "est le plus petit nombre")
