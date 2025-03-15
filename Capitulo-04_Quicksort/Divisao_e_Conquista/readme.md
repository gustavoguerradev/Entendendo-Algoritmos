# Divisão e Conquista


Divisão e Conquista é uma técnica de resolução de problemas que envolve dividir um problema maior em subproblemas menores, resolvendo cada um deles separadamente e, em seguida, combinando as soluções para obter o resultado final. Essa abordagem é especialmente eficiente para problemas que podem ser reduzidos recursivamente em partes menores.

## Como funciona?
A estratégia de Divisão e Conquista segue três etapas principais:

1. **Divisão**: O problema é dividido em partes menores, geralmente de tamanho igual ou similar.
2. **Conquista**: Cada subproblema é resolvido de forma independente, muitas vezes recursivamente.
3. **Combinação**: As soluções dos subproblemas são combinadas para formar a solução final.

## Exemplo: Pesquisa Binária
A pesquisa binária é um exemplo clássico do uso de Divisão e Conquista. O algoritmo busca um elemento dentro de uma lista ordenada, reduzindo pela metade o espaço de busca a cada iteração.

### Passos da Pesquisa Binária:
1. **Divisão**: Encontramos o meio da lista e comparamos com o elemento desejado.
2. **Conquista**: Se o elemento do meio for o alvo, retornamos sua posição. Se for menor, repetimos a busca na metade esquerda. Se for maior, na metade direita.
3. **Combinação**: A resposta vem diretamente da recursão, sem necessidade de combinação explícita.

### Código em Python (Recursivo):
```python
def pesquisa_binaria_recursiva(lista, item, baixo, alto):
    if baixo > alto:
        return None
    
    meio = (baixo + alto) // 2
    chute = lista[meio]
    
    if chute == item:
        return meio
    elif chute > item:
        return pesquisa_binaria_recursiva(lista, item, baixo, meio - 1)
    else:
        return pesquisa_binaria_recursiva(lista, item, meio + 1, alto)
```

## Vantagens e Desvantagens
### ✅ Vantagens
- Redução significativa do tempo de execução em muitos casos.
- Algoritmos eficientes e elegantes.
- Aplicável a uma ampla gama de problemas.

### ❌ Desvantagens
- Nem todos os problemas podem ser resolvidos de forma eficiente com essa abordagem.
- Pode ter sobrecarga de chamadas recursivas, aumentando o consumo de memória.
