x = 1
sumaedades = 0
sumaedadesMuj = 0
sumaedadesHom = 0
muj = 0
hom = 0
personas = int(input("ingrese la  cantidad de personas: "))
while x <= personas:
	edad = int(input("ingrese la edad: "))
	genero = input("su genero es F o M: ")
	sumaedades = sumaedades + edad
	if genero == "F":
		muj = muj + 1
		sumaedadesMuj = sumaedadesMuj + edad
	elif genero == "M":
		hom = hom + 1
		sumaedadesHom = sumaedadesHom + edad
	x = x + 1
print("el promedio de todas las edades es: ",sumaedades / personas)
print("el numero de mujeres es: ",muj)
print("el promedio de edad de las mujeres es: ",sumaedadesMuj / muj)
print("el numero de hombres es: ",hom)
print("el promedio de edad de lo hombres es: ",sumaedadesHom / hom)
