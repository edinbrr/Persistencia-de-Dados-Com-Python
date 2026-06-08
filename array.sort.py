# Array de números

numeros = [45, 12, 78, 3, 90, 22, 1, 65, 34, 8, 50, 99, 17, 27, 5]

print("Original:")
print(numeros)

numeros.sort()

print("\nCrescente:")
print(numeros)

numeros.sort(reverse=True)

print("\nDecrescente:")
print(numeros)

# Array de strings

dados = [
    "Edson Victor",
    "15/06/1998",
    "12345678900",
    "200100200"
]

print("\nStrings Original:")
print(dados)

dados.sort()

print("\nStrings Crescente:")
print(dados)

dados.sort(reverse=True)

print("\nStrings Decrescente:")
print(dados)