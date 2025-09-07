
L1 = float(input("Primer lado: "))
L2 = float(input("Segundo lado: "))
L3 = float(input("Tercer lado: "))

if L1 == L2 == L3:
    print("Triangulo equilátero.")
elif L1 == L2 or L1 == L3 or L2 == L3:
    print("Triangulo isoceles")
else:
    print("Triangulo escaleno.")