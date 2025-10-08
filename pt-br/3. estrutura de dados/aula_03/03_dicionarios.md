# 🟨 Dicionários (`dict`) em Python

## 📌 O que são?

Um dicionário é uma **estrutura de dados que armazena pares de chave → valor**. **É uma coleção mutável, desordenada (até o Python 3.6)** e *indexada por chave, não por posição.*

```python

# Exemplo de dicionário
aluno = {"nome": "Carlos", "idade": 20, "curso": "Python"}
print(aluno["nome"])  # saída: Carlos
```

> ✅ Aqui já temos múltiplos valores (nome, idade, curso) armazenados em um único dicionário.

## 🔁 Dicionário aninhado (múltiplos valores por registro)

```python
# Cadastro de funcionários com informações aninhadas
funcionarios = {
    1: {"nome": "Lucas Andrade", "idade": 20, "salario": 1564.20},
    2: {"nome": "Gabriel Morais", "idade": 22, "salario": 1445.60},
    3: {"nome": "Victor Leon", "idade": 25, "salario": 1321.80}
}

# Adicionando um novo funcionário
funcionarios[4] = {"nome": "Ana Paula", "idade": 23, "salario": 1400.00}

# Atualizando o salário de um funcionário
funcionarios[2]["salario"] = 1500.00
```

## 🔎 Acessando valores

```python
# Acessando valores de um dicionário simples
print(aluno["nome"])  # Carlos

# Acessando valores em dicionário aninhado
print(funcionarios[1]["salario"])  # 1564.20
```

### 🔑 Características principais

* As **chaves são únicas**.
* Os **valores podem ser de qualquer tipo**.
* As chaves normalmente são `str`, `int`, ou `tuple` imutáveis.

## 🧰 Principais métodos e operações

| Método      | Descrição                                          |
| ----------- | -------------------------------------------------- |
| `dict[key]` | Acessa o valor da chave `key`.                     |
| `get(key)`  | Retorna o valor da chave ou `None` se não existir. |
| `keys()`    | Retorna todas as chaves.                           |
| `values()`  | Retorna todos os valores.                          |
| `items()`   | Retorna os pares (chave, valor).                   |
| `update()`  | Atualiza com novos pares.                          |
| `pop(key)`  | Remove o par com a chave dada.                     |

### 🧪 Exemplos práticos

#### Exemplo prático 01

```python
livro = {
    "título": "Python Básico",
    "autor": "João Silva",
    "ano": 2025
}

# Acessar o título do livro
print(livro["título"])

# Adicionar novo par, número de páginas 
livro["páginas"] = 300

# Atualizar valor do ano 
livro["ano"] = 2024

# Iterar sobre o dicionário
for chave, valor in livro.items():
    print(f"{chave}: {valor}")
```

#### Exemplo prático 02

```python
aluno = {"nome": "Carlos", "idade": 20, "curso": "Python"}

# Usando get()
print(aluno.get("nome"))        # Carlos
print(aluno.get("email", "Não informado"))  # valor padrão

# Listando chaves e valores
print(aluno.keys())    # dict_keys(['nome', 'idade', 'curso'])
print(aluno.values())  # dict_values(['Carlos', 20, 'Python'])

# Removendo um item
aluno.pop("curso")
print(aluno)           # {'nome': 'Carlos', 'idade': 20}
```

## ✅ Quando usar?

* Quando você precisa **associar um dado a uma chave significativa**.
* Para **armazenar atributos de um objeto**, como em um cadastro.

---

## 📝 Conclusão

Agora que você entendeu como funcionam os dicionários em Python, é hora de praticar!

> ✅ **Desafio sugeridos:** *Catalógo de Filmes*

1. Crie um dicionário que represente um filme, com informações como título, diretor, ano e gênero.
2. Atualize os valores, adicione novos pares e remova uma chave.
3. Percorra os itens com um for e exiba todas as informações de forma formatada.

> Praticar é a melhor forma de consolidar o aprendizado! Teste diferentes combinações, explore os métodos e abuse do print() para observar os resultados.

**Próximo arquivo [Set](04_set.md)**

---

### 📝 Exercícios Moderados — Dicionários

* *Cadastro de funcionários*

Crie um dicionário para armazenar informações de 3 funcionários (nome, idade, salário). Depois:

1. Atualize o salário de um funcionário específico.
2. Remova um funcionário do cadastro.
3. Percorra o dicionário e exiba o nome e salário de cada funcionário.

* *Notas de alunos*

Crie um dicionário com alunos como chaves e suas notas como valores. Depois:

1. Calcule a média da turma.
2. Atualize a nota de um aluno específico.
3. Liste os alunos com nota acima da média.

* *Agenda de contatos*

Crie um dicionário onde as chaves são nomes e os valores são listas com telefone e e-mail. Depois:

1. Adicione um novo contato.
2. Atualize o telefone de um contato existente.
3. Remova um contato que não é mais necessário.
4. Liste todos os contatos com seus dados formatados.

**[Gabarito](exercicios/README.md)**
