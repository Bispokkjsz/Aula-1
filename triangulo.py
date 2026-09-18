# Crie um algoritimo que leia tres valores (lados de um triangulo)
# Determine se formam  um triangulo
# se é um equilatero, isoceles ou escaleno

a = float(input("Qual o seu primeiro lado? "))
b = float(input("Qual o seu segundo lado? "))
c = float(input("Qual o seu terceiro lado? "))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print("é um triangulo equilatero")
    elif a == b or b == c or c == a:
        print("é um triangulo isoceles")
    else:
        print("é um triangulo escaleno")
else:
    print("Nao é um triangulo")
    