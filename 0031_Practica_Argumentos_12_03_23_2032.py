#Ejercicio
#1.-¿Cuántos argumentos se utilizan en cada una de estas llamadas?	

def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')  #Tiene 4 argumentos
colores('lila', 'negro', 'rojo')            # Tiene 3 arguentos
colores('rosa')          #Tiene 1 argumento
colores('marrón', 'naranja')   #Tiene 2 argumentos

#2.-Completa el siguiente fragmento de código:

def col(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

col('rojo','verde') #Faltaba asignar el valor de los argumentos

#3.-Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*args):  #Se declara la funcion con argumentos
  res = args[0] + args[1] + args[2] + args[3] + args[4]  #Se hace la suma
  print(res)    #Se imprime el resultado
  
suma(18,11,20,1,5) #Se manda a llamar la suma
