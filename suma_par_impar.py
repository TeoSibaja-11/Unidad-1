N = int(input("Ingresa un numero: "))

SP = 0
SI = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        SP += i
    else:
        SI += i

print(f"Suma de pares: {SP}")
print(f"Suma de impares: {SI}")
