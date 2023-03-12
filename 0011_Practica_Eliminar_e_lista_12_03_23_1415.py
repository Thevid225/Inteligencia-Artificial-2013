#Ejercicio 
#De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'. Debes utilizar al menos una vez las posiciones negativas para eliminar un color. Después, imprime la lista para ver los colores que se han eliminado.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
del colores[1]
del colores[3] #Al eliminar uno se mueve la lista
del colores[-4] #La lista no se mueve si el numero es antes del que se va a eliminar despues 
del colores[-3]

print (colores) 
