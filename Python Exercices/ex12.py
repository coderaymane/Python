n = int(input("Entrez le nombre de termes de la série de Fibonacci : "))
a, b = 0, 1
print("Série de Fibonacci :", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
