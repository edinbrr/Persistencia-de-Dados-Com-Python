# DGT2819 - Persistência de Dados com Python

Projeto desenvolvido para a disciplina **DGT2819 – Persistência de Dados com Python**, com o objetivo de aplicar conceitos fundamentais de manipulação de dados, leitura e escrita de arquivos e algoritmos de ordenação utilizando a linguagem Python.

## Objetivos

* Implementar ordenação de listas utilizando o método nativo `sort()`;
* Desenvolver os algoritmos de ordenação **Bubble Sort** e **Selection Sort**;
* Realizar leitura de dados a partir de arquivos `.txt`;
* Efetuar escrita de dados em arquivos externos;
* Comparar o desempenho dos diferentes métodos de ordenação;
* Construir um MVP para criação de um glossário de palavras ordenadas a partir de documentos de texto.

## Estrutura do Projeto

```text
.
├── array.sort.py
├── bubble.sort.py
├── selection.sort.py
├── ler.txt.py
├── escrever.txt.py
├── kdd.py
├── loremipsum.txt
├── texto.txt
└── palavras_ordenadas.txt (gerado automaticamente)
```

### Arquivos

* `array.sort.py` → Ordenação de listas utilizando o método nativo `sort()`;
* `bubble.sort.py` → Implementação do algoritmo Bubble Sort;
* `selection.sort.py` → Implementação do algoritmo Selection Sort;
* `ler.txt.py` → Leitura de dados em arquivos texto;
* `escrever.txt.py` → Escrita de dados em arquivos texto;
* `kdd.py` → Projeto principal com leitura de documentos, separação de palavras, ordenação e análise de desempenho dos algoritmos;
* `loremipsum.txt` → Arquivo utilizado para os testes de leitura;
* `texto.txt` → Arquivo contendo as palavras utilizadas pelo projeto principal;
* `palavras_ordenadas.txt` → Arquivo gerado automaticamente pelo sistema contendo as palavras ordenadas.

## Tecnologias Utilizadas

* Python 3
* Visual Studio Code

## Funcionalidades

* Leitura de arquivos texto;
* Escrita de dados em arquivos externos;
* Manipulação de listas;
* Separação de conteúdo em palavras;
* Ordenação utilizando diferentes algoritmos;
* Comparação de tempo de execução;
* Geração automática de arquivo contendo as palavras ordenadas.

## Como Executar

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Acessar a pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Executar as atividades individuais

#### Ordenação com sort()

```bash
python array.sort.py
```

#### Bubble Sort

```bash
python bubble.sort.py
```

#### Selection Sort

```bash
python selection.sort.py
```

#### Leitura de Arquivos

```bash
python ler.txt.py
```

#### Escrita de Arquivos

```bash
python escrever.txt.py
```

Este comando irá criar automaticamente o arquivo:

```text
texto.txt
```

### 4. Executar o Projeto Final

Após garantir que o arquivo `texto.txt` existe na pasta do projeto:

```bash
python kdd.py
```

### Saída Esperada

O sistema exibirá no terminal:

* Tempo de execução do Bubble Sort;
* Tempo de execução do Selection Sort;
* Tempo de execução do método nativo `sort()`;
* Lista de palavras ordenadas.

Exemplo:

```text
===== RESULTADOS =====

Bubble Sort: 0.000001 segundos
Selection Sort: 0.000001 segundos
Sort Nativo: 0.000000 segundos

Arquivo palavras_ordenadas.txt criado com sucesso.
```

Ao final da execução será criado automaticamente o arquivo:

```text
palavras_ordenadas.txt
```

contendo todas as palavras ordenadas alfabeticamente.

## Resultados Obtidos

Durante os testes foi possível observar que o método nativo `sort()` do Python apresentou melhor desempenho em comparação aos algoritmos Bubble Sort e Selection Sort, tornando-se a alternativa mais eficiente para ordenação de grandes quantidades de dados.

## Autor

**Edson Victor Miranda**

Disciplina: DGT2819 – Persistência de Dados com Python
Curso: Análise e Desenvolvimento de Sistemas
