N = int(input("Ingresa un numero entero: "))

NI = str(abs(N))[::-1]

if N < 0:
    NI = '-' + NI

print(f"Numero invertido: {NI}")
