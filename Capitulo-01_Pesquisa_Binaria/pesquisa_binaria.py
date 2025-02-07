def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1
    return None # Caso nosso alvo não exista

lista = [2,4,7,8,9,11,12,19,22,24,33]
alvo = 22
print(pesquisa_binaria(lista, alvo)) # -> 8

