#Ejercicio
#Haz una tupla que contenga cuatro colores de tu elección. Tendrás que poner una condición con el condicional if para cada color que le avise al usuario que el color está en la tupla con un mensaje como este: print('El color rojo está admitido') y una condición False para contemplar cualquier color que no esté en la tupla con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Además tendrás que hacer esto con un input() que permita introducir un color al usuario.

colores=('verde','rojo','azul','blanco')

entrada = input('Introduce un color:\n') #Se obtiene un valor del teclado
if entrada in colores:   #compara los valores de entrada y la tupla
    print('El color que buscas está en la tupla.')
else:
    print('El color que buscas no está en la tupla.')
