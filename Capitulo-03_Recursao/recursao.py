def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x -1)

print(fatorial(5)) #120

#Usando apenas caso-base
def fatorial_caso_base(n):
    resultado = 1  # Caso-base: fatorial de 0 ou 1 é 1
    for i in range(2, n + 1):  # Começa de 2 até n
        resultado *= i  # Multiplica o resultado atual por i
    return resultado

print(fatorial_caso_base(5))