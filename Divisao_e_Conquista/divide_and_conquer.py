# Explicação sobre Divisão e Conquista
# Para explicar Divisão e Conquista, podemos usar a pesquisa binária como exemplo.
# Essa técnica resolve um problema ao dividi-lo em subproblemas menores, resolvendo cada um individualmente e combinando os resultados.
# Na pesquisa binária, em cada etapa, dividimos a lista pela metade, reduzindo o espaço de busca.
# Se o valor do meio for o alvo, retornamos o índice.
# Se o alvo for menor que o meio, continuamos a busca na metade esquerda.
# Se for maior, buscamos na metade direita.
# Esse processo continua até encontrarmos o elemento ou esgotarmos as possibilidades

def pesquisa_binaria_recursiva(lista, item, baixo, alto):
    if baixo > alto:
        return None  # Caso nosso alvo não exista

    meio = (baixo + alto) // 2
    chute = lista[meio]

    if chute == item:
        return meio
    elif chute > item:
        return pesquisa_binaria_recursiva(lista, item, baixo, meio - 1)
    else:
        return pesquisa_binaria_recursiva(lista, item, meio + 1, alto)


lista = [2, 4, 7, 8, 9, 11, 12, 19, 22, 24, 33]
alvo = 11
resultado = pesquisa_binaria_recursiva(lista, alvo, 0, len(lista) - 1)
print(resultado)  # -> 5


#Exercicio 4.1 do livro, fazer uma funcão soma usando recursão
def soma(lista):
    if not lista:
        return 0
    else:
        return lista.pop(0) + soma(lista) ## O POP REMOVE E RETORNA

print(soma([2,4,6]))