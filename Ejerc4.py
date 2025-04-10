def encontrar_maximo_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c   

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    maximo = encontrar_maximo_tres(num1, num2, num3)
    
    print(f"El valor máximo entre {num1}, {num2} y {num3} es: {maximo}")

if __name__ == "__main__":
    main()