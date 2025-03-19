## 📜 Resumo Teórico - QuickSort

O **QuickSort** é um dos algoritmos de ordenação mais eficientes, baseado na técnica de **divisão e conquista**. Ele escolhe um elemento como **pivô**, particiona a lista em duas partes (elementos menores e maiores que o pivô) e, então, ordena essas partes recursivamente. Apesar de ser mais eficiente que o algoritmo de ordenação por seleção, ele ainda não é o melhor, pois em seu pior caso, ainda vamos ter um tempo de execução de O(n²)

### 🔹 Funcionamento:
1. Escolhe-se um **pivô** na lista.
2. Os elementos menores que o pivô são colocados à esquerda e os maiores à direita.
3. O processo é repetido recursivamente nas duas sublistas até que todas estejam ordenadas.
4. A junção das sublistas resulta na lista ordenada.

### 🔹 Implementação (Python):
```python
# Função QuickSort
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
```

### 🔹 Vantagens:
1. **Rápido na prática**, com tempo médio de **O(n log n)**.
2. **Uso eficiente de memória**, pois a ordenação ocorre **in-place** na maioria das implementações.
3. **Bom desempenho para grandes conjuntos de dados**.

### 🔹 Desvantagens:
1. **Pior caso O(n²)** ocorre se o pivô escolhido for o menor ou maior elemento em cada partição.
2. **Não é estável**, ou seja, pode alterar a ordem de elementos iguais.

### 🔹 Complexidade:
- **Melhor caso**: O(n log n) (quando o pivô divide a lista equilibradamente).
- **Médio caso**: O(n log n) (na maioria das implementações práticas).
- **Pior caso**: O(n²) (quando a partição é muito desigual).



