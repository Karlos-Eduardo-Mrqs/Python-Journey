# 🟨 Dicionários (`dict`) em Python

## 📌 O que são?

Um **dicionário** é uma estrutura de dados que armazena pares de **chave → valor**. É uma coleção **mutável**, **desordenada** (até o Python 3.6) e **indexada por chave**, não por posição.

```python
# Exemplo de dicionário
aluno = {"nome": "Carlos", "idade": 20, "curso": "Python"}
print(aluno["nome"])  # saída: Carlos
```

## 🔑 Características principais

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

### 🧪 Exemplo prático

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

## ✅ Quando usar?

* Quando você precisa **associar um dado a uma chave significativa**.
* Para **armazenar atributos de um objeto**, como em um cadastro.

---

## 📝 Conclusão

Agora que você entendeu como funcionam os dicionários em Python, é hora de praticar!

✅ **Desafios sugeridos:**

1. Crie um dicionário que represente um filme, com informações como título, diretor, ano e gênero.
2. Atualize os valores, adicione novos pares e remova uma chave.
3. Percorra os itens com um for e exiba todas as informações de forma formatada.

> Praticar é a melhor forma de consolidar o aprendizado! Teste diferentes combinações, explore os métodos e abuse do print() para observar os resultados.

**Próximo arquivo [Set](./set.md)**