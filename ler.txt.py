arquivo = open("loremipsum.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print("Conteúdo completo:")
print(conteudo)

arquivo.close()

arquivo = open("loremipsum.txt", "r", encoding="utf-8")

print("\nPrimeira linha:")
print(arquivo.readline())

arquivo.close()

arquivo = open("loremipsum.txt", "r", encoding="utf-8")

print("\nPrimeiros 3 caracteres:")
print(arquivo.read(3))

arquivo.close()

print("\nUsando WITH:")

with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())