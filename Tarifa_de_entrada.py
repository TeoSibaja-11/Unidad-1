edad = int(input("Dime cual es tu edad: "))

if edad < 12:
    costo = 50
elif edad <= 17:
    costo = 80
else:
    costo = 120

print(f"Costo de entrada: ${costo}")
