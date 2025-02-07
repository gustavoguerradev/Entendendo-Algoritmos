## 📜 Resumo Teórico - Capítulo 1: Busca Binária
A **busca binária** é um algoritmo eficiente para encontrar um elemento em uma lista ordenada. Ela segue a estratégia de dividir a lista ao meio repetidamente, reduzindo o espaço de busca a cada iteração.

### 🔹 Funcionamento:
1. Comparar o elemento do meio com o valor desejado.
2. Se forem iguais, o elemento foi encontrado.
3. Se o valor desejado for menor, a busca continua na metade esquerda.
4. Se for maior, a busca continua na metade direita.
5. O processo se repete até encontrar o elemento ou esgotar a lista.

### 🔹 Complexidade:
- Melhor caso: **O(1)** (quando o elemento está no meio da lista na primeira verificação).
- Caso médio e pior caso: **O(log n)** (pois reduz a busca pela metade a cada iteração).
