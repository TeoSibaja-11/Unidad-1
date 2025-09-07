N = int(input("Dame la altura de la piramide: "))

for i in range(1, N + 1):
    E = ' ' * (N - i)
    A = '*' * (2 * i - 1)
    print(E + A)
