## 📜 Resumo Teórico - Capítulo 2: Ordenação por Seleção
A **Ordenação por Seleção** é um algoritmo simples e intuitivo para ordenar listas. Ele funciona encontrando o menor elemento e colocando-o na posição correta, repetindo esse processo até que toda a lista esteja ordenada.

### 🔹 Funcionamento:
1. Percorre a lista e encontra o indice do menor elemento.
2. Armazena o menor valor encontrado e adiciona ele a um novo array.
3. Repete o processo para o restante da lista (ignorando os elementos já ordenados).
4. Continua até que toda a lista esteja ordenada.

### 🔹 Complexidade:
1. Melhor, médio e pior caso: O(n²) (pois percorre a lista para encontrar o menor em cada iteração).
2. Desvantagem: Ineficiente para listas grandes.
3. Vantagem: Simples de implementar e não precisa de memória extra.