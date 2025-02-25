## 📜 Resumo Teórico - Capítulo 3: Recursão

A **Recursão** é uma técnica de programação onde uma função chama a si mesma para resolver um problema. É usada para dividir problemas complexos em subproblemas menores e mais fáceis de resolver.

### 🔹 Funcionamento:
1. Define-se um **caso base**, que interrompe as chamadas recursivas.
2. Em cada chamada, o problema é reduzido, aproximando-se do caso base.
3. Quando o caso base é alcançado, as chamadas começam a retornar os resultados.
4. O problema completo é resolvido ao combinar as soluções dos subproblemas.

### 🔹 Exemplo Clássico:
Cálculo do fatorial de um número:

```
função fatorial(x):
  se n == 1:
    retorne 1
  senão:
    retorne n * fatorial(x - 1)
```

### 🔹 Vantagens:
1. Simplicidade e clareza no código, principalmente para problemas que têm uma natureza recursiva (ex.: árvores, grafos).
2. Reduz a complexidade em problemas que seriam difíceis de resolver iterativamente.

### 🔹 Desvantagens:
1. Pode ser ineficiente em termos de memória, devido ao uso da pilha de chamadas.
2. Risco de **stack overflow** se o caso base não for alcançado corretamente.

### 🔹 Complexidade:
- Depende do problema específico.
- No cálculo de fatorial, por exemplo, a complexidade é O(n), pois faz n chamadas recursivas.

### 🔹 Dicas:
1. Sempre defina um caso base claro.
2. Certifique-se de que as chamadas recursivas estão progredindo para o caso base.
3. Em problemas mais complexos, considere usar **memorização** (armazenar resultados já calculados) para melhorar a eficiência.
