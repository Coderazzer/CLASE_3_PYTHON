'''Pedir al usuario una lista de numeros separados por comas y ordenarlos
usando bubble sort, se deben imprimir ordenados en 1 sola linea'''

string = input('Introducir numeros separados por una coma:\n')

list = string.split(',')

for n in range(len(list)):
 
    for m in range(0, len(list) - n - 1):

      if list[m] > list[m + 1]:

        list[m], list[m+1] = list[m+1], list[m]

print('Lista Ordenada:')
print(list)