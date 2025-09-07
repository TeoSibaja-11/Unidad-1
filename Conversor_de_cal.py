Cal = int(input("Ingresa la calificación entre 0 y 100: "))


if Cal >= 90:
    letra = "A"
elif Cal >= 80:
    letra = "B"
elif Cal >= 70:
    letra = "C"
elif Cal >= 60:
    letra = "D"
else:
    letra = "F"

print(f"Tu calificación en letra es: {letra}")
