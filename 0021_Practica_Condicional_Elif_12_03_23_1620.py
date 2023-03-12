#Ejercicio
#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.

edad = int(input('¿Cuál es tu edad?\n'))

if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45: #Se cambia el 100 por el nuevo limite
	print('Eres mayor de edad.')
elif edad >= 45 and edad <= 100:  #Se agrega el elif nuevo e 45 a 100
	print('Eres de tercera edad.')
else:
	print('Edad no válida.')
