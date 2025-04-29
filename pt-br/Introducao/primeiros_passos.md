# Primeiros Passos
Agora com o ambiente configurado anteriormente, podemos iniciar os nossos primeiros passos com a programação em python !

# Variáveis 
As variáveis são usadas para armazenar informações que poderão ser manipuladas ao longo do programa. Em Python, criar uma variável é simples e não exige a definição do tipo de dado (como ocorre em outras linguagens, Java ou C++ ).

# 🧠 Regras para Nomeação de Variáveis

| Regra | Descrição |
|:------|:----------|
| Começar com letra ou `_` | O nome da variável deve iniciar com uma letra (a-z, A-Z) ou underline (`_`). |
| Letras, números e underscores | Após o primeiro caractere, o nome pode conter letras, números e underscores. |
| Não começar com número | Variáveis **não podem** começar com números. |
| Case-sensitive | Python diferencia maiúsculas e minúsculas (`nome`, `Nome` e `NOME` são variáveis diferentes). |
| Evitar palavras reservadas | Não utilize palavras-chave da linguagem (como `class`, `if`, `for`) como nomes de variáveis. |

> Boas práticas: use nomes descritivos que deixem claro o que a variável representa.

# ✅ Exemplos de Nomes de Variáveis

| Nome | Tipo | Observação |
|:-----|:--------|:-----------|
| nome | Válido | Apenas letras minúsculas. |
| for | Inválido | `for` é uma palavra reservada em Python. |
| Nome_Completo | Válido | Uso de letra maiúscula e underscore. |
| idade29 | Válido | Pode ter números, mas **não no início**. |
| class | Inválido | `class` é uma palavra reservada em Python. |
| _endereco | Válido | Começar com underscore é permitido. |
| 29idade | Inválido | Não pode começar com número. |
| nome completo | Inválido | Espaços não são permitidos; use `_`. |

# Tipos de Dados
Em Python, os tipos de dados determinam o tipo de valor que uma variável pode armazenar. Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa declarar o tipo da variável explicitamente.

# 🔹 Tabela Dos Tipos de Dados em Python

| Tipo de Dado | Descrição | Exemplo de Código | Exemplo na Vida Real |
|:-------------|:----------|:------------------|:---------------------|
| **int** | Números inteiros (sem casas decimais). | `idade = 30` | Idade de uma pessoa: `30 anos` |
| **float** | Números com casas decimais. | `altura = 1.75` | Altura de uma pessoa: `1,75 metros` |
| **str** | Sequências de caracteres (texto). | `nome = "Carlos"` | Nome de um aluno: `"Carlos"` |
| **bool** | Valores booleanos (`True` ou `False`). | `is_student = True` | Se a pessoa está matriculada: `True` |
| **list** | Coleções ordenadas e mutáveis. | `frutas = ["maçã", "banana", "laranja"]` | Lista de compras no mercado. |
| **tuple** | Coleções ordenadas e imutáveis. | `coordenadas = (10, 20)` | Localização GPS: `(latitude, longitude)` |
| **dict** | Coleções de pares chave-valor. | `aluno = {"nome": "Carlos", "idade": 20}` | Ficha de cadastro de um aluno. |

# 📚 Explicação Rápida
- **Inteiros (int):** São usados para contar, identificar ou enumerar.

- **Floats (float):** Representam valores fracionários, como alturas e medidas.

- **Strings (str):** São textos que podem incluir letras, números e símbolos.

- **Booleanos (bool):** Representam apenas dois estados: verdadeiro ou falso.

- **Listas (list):** Guardam uma sequência de valores que podem ser alterados.

- **Tuplas (tuple):** Guardam uma sequência que não pode ser alterada.

- **Dicionários (dict):** Armazenam dados em pares (chave e valor), como uma ficha de informações.

## ✅ Exemplo Prático Combinado

```python
nome = "Ana"                  # str
idade = 25                    # int
altura = 1.68                 # float
estudante = True              # bool
materias = ["Python", "SQL", "Git"]  # list
coordenadas = (34.5, -120.7)          # tuple
perfil = {"nome": "Ana", "idade": 25} # dict
```

# Comandos de Entrada e Saída
Agora que você já entende variáveis e tipos de dados, vamos aprender a interagir com o usuário!

Python possui funções simples para entrada e saída de dados:

---

# 🔹 Saída de Dados: `print()`

O comando `print()` é usado para exibir informações no console.

### Exemplos:
> Começo:

```python
print("Olá, mundo!")
print("A soma de 2 + 3 é:", 2 + 3)
```

> Saída:

```bash
Olá, mundo!
A soma de 2 + 3 é : 5 
```

# 🔹 Entrada de Dados: `input()`
O comando `input()` permite receber dados do usuário.

### Exemplo:

```python
nome = input("Digite seu nome: ")
print("Seja bem-vindo(a),", nome)
```

> Funcionamento:

O programa irá pausar e esperar o usuário digitar algo.

Tudo o que for digitado será armazenado como string.

## ⚡ Atenção!
Por padrão, o que for lido pelo input() será do tipo str (texto), mesmo que o usuário digite números! 

**Para converter o tipo, usamos o casting:**

Exemplo de conversão:

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

- **int() :** converte para inteiro.
- **float() :** converte para ponto flutuante.