
numero = int(input("Dame el numero entero: "))
n = abs(numero)
contador = 0

if n == 0:
    contador = 1 
else:
    while n > 0:
        n //= 10
        contador += 1
print(f"El numero {numero} tiene {contador} digitos")
