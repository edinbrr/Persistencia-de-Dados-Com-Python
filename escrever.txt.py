texto = list()

texto.append("Direito Civil")
texto.append("Direito Penal")
texto.append("Jurisprudencia")
texto.append("Processo Judicial")
texto.append("Advocacia")

with open("texto.txt", "w", encoding="utf-8") as arquivo:

    for linha in texto:
        arquivo.write(linha + "\n")

print("Arquivo texto.txt criado com sucesso.")