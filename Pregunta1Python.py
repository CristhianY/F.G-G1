print("Introduce primera calificacion")
parcial1=input()
print("Introduce segunda calificacion")
parcial2=input()
print("Introduce tercera calificacion")
parcial3=input()
print("Introduce nota de tabajo")
Trabajo1=input()

calif1= int(parcial1)*(10/100)
calif2= int(parcial2)*(15/100)
calif3= int(parcial3)*(25/100)
calif4= int(Trabajo1)*(50/100)

suma=calif1+calif2+calif3+calif4
promedio=suma

print("Tu promedio final es: %d"%promedio)
