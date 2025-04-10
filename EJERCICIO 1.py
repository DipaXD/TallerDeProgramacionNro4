def encontrar_maximo_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def probar_maximo_tres():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    
    maximo = encontrar_maximo_tres(num1, num2, num3)
    print(f"El máximo entre {num1}, {num2} y {num3} es: {maximo}")

    probar_maximo_tres()