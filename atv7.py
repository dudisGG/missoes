# 1. Perguntar quantos números a pessoa quer digitar
quantidade = int(input("Quantos números você vai digitar? "))

# 2. Ler todos os números e guardar na primeira lista
numeros = []
for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# 3. Montar uma segunda lista apenas com os números pares
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

# 4. Mostrar os resultados
print("\n--- Resultados ---")
print(f"Lista completa de números: {numeros}")
print(f"Lista de números pares: {pares}")
print(f"Total de números pares encontrados: {len(pares)}")