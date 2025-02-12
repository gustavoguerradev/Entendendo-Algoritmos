def buscaMenor(arr):  #Percorre o arr e retorna o indice do menor elemento.
    menor_valor = arr[0]
    menor_indice = 0
    for i in range(1,len(arr)):
        if arr[i] < menor_valor:
            menor_valor = arr[i]
            menor_indice = i

    return menor_indice

def ordenacaoPorSelecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novo_arr.append(arr.pop(menor)) ##Remove e retorna o menor elemento do arr
    return novo_arr

arr_desorganizado = [2,7,1,4,6]
arr_organizado = ordenacaoPorSelecao(arr_desorganizado)

print(arr_organizado)