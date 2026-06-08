import time


def bubble_sort(lista):

    lista = lista.copy()

    for i in range(len(lista)):

        for j in range(0, len(lista) - i - 1):

            if lista[j].lower() > lista[j + 1].lower():

                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def selection_sort(lista):

    lista = lista.copy()

    for i in range(len(lista)):

        menor = i

        for j in range(i + 1, len(lista)):

            if lista[menor].lower() > lista[j].lower():
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


palavras = []

with open("texto.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:

        palavras.extend(linha.split())


inicio = time.time()
resultado_bubble = bubble_sort(palavras)
tempo_bubble = time.time() - inicio

inicio = time.time()
resultado_selection = selection_sort(palavras)
tempo_selection = time.time() - inicio

inicio = time.time()
resultado_sort = sorted(palavras, key=str.lower)
tempo_sort = time.time() - inicio

print("\n===== RESULTADOS =====")

print(f"\nBubble Sort: {tempo_bubble:.10f} segundos")
print(resultado_bubble)

print(f"\nSelection Sort: {tempo_selection:.10f} segundos")
print(resultado_selection)

print(f"\nSort Nativo: {tempo_sort:.10f} segundos")
print(resultado_sort)

with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo:

    for palavra in resultado_sort:

        arquivo.write(palavra + "\n")

print("\nArquivo palavras_ordenadas.txt criado com sucesso.")