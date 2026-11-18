# Criando uma lista vazia para armazenar as notas
notas = []

# Lendo 4 notas usando um loop
for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

# Calculando a soma e a média
soma_notas = sum(notas)
media_notas = soma_notas / len(notas)

# Exibindo os resultados de forma organizada
print("\n--- Resultados ---")
print(f"Lista de notas: {notas}")
print(f"Soma das notas: {soma_notas:.2f}")
print(f"Média das notas: {media_notas:.2f}")