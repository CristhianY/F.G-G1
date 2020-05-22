puntos=float(input("Ingrese puntos ganados"))
bono=float(input("Ingrese salario minimo"))
if puntos <= 100:
    bono = (bono * 0.10)
    print("tu bono es de",bono)
elif 100 <= puntos <= 150:
    bono = (bono * 0.5)
    print("tu bono es de",bono)
elif 150 <= puntos <= 250:
    bono = (bono * 1)
    print("tu bono es de",bono)
