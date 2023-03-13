#Ejercicio
#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1  #Se elimina todo el teclado 1

del teclado2['Categoria'] #Eliminamos la categoria del teclado 2
del teclado2['Precio']    #Eliminamod el precio del teclado 2
print (teclado2['Modelo']) #Imprimimos lo que queda
