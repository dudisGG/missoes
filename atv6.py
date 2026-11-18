num = [12, 45, 7, 30, 2, 19]

# --- 1. Encontrando o maior e o menor usando for e if ---
maior = num[0]
menor = num[0]

for n in num:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"Lista analisada: {num}")
print(f"[For/If] O maior número é: {maior}")
print(f"[For/If] O menor número é: {menor}")

print("-" * 30)

# --- 2. Conferindo com max() e min() ---
maior_verificacao = max(num)
menor_verificacao = min(num)

print(f"[max/min] O maior número é: {maior_verificacao}")
print(f"[max/min] O menor número é: {menor_verificacao}")