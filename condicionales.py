# Declaramos una variable
calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)

# Preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("Veees, por no estudiar") # Si es menor a 700 muestra esto
elif calificacion > 1000 :
    print("MIENTESS!!!! No puedes sacar más de mil")
else : # Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenid@ al mamitas")
elif edad > 100 :
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajer@ del tiempo")
else :
    print("No puedes llevarte esos cigarros")