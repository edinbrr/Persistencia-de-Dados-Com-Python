numeros = [45, 12, 78, 3, 90, 22, 1, 65, 34, 8, 50, 99, 17, 27, 5]

for i in range(len(numeros)):

    menor = i

    for j in range(i + 1, len(numeros)):

        if numeros[menor] > numeros[j]:
            menor = j

    numeros[i], numeros[menor] = numeros[menor], numeros[i]

print(numeros)