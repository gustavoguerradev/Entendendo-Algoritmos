def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

lista = [2,6,1,4,0,20,12,-1]
lista_ordenada = quicksort(lista)
print(lista_ordenada)

