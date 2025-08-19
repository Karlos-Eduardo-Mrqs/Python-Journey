# Primeiros Passos 🐍

Agora que você já configurou seu ambiente, podemos iniciar nossos primeiros passos com a programação em Python!

---

## 📦 Variáveis

As variáveis são usadas para armazenar informações que podem ser manipuladas ao longo do programa. Em Python, criar uma variável é simples e não exige a definição do tipo de dado (como ocorre em linguagens como Java ou C++).

---

## 🧠 Regras para Nomeação de Variáveis

| Regra                         | Descrição                                                                            |
| :---------------------------- | :----------------------------------------------------------------------------------- |
| Começar com letra ou `_`      | O nome deve iniciar com uma letra (a-z, A-Z) ou underline (`_`).                     |
| Letras, números e underscores | Após o primeiro caractere, pode conter letras, números e underscores.                |
| Não começar com número        | Variáveis **não podem** começar com números.                                         |
| Case-sensitive                | Python diferencia maiúsculas de minúsculas (`nome`, `Nome` e `NOME` são diferentes). |
| Evitar palavras reservadas    | Não utilize palavras-chave da linguagem (como `class`, `if`, `for`).                 |

> **💡 Boas práticas:** use nomes descritivos que deixem claro o que a variável representa.

---

## ✅ Exemplos de Nomes de Variáveis

| Nome           | Tipo     | Observação                           |
| :------------- | :------- | :----------------------------------- |
| nome           | Válido   | Apenas letras minúsculas.            |
| for            | Inválido | Palavra reservada.                   |
| Nome\_Completo | Válido   | Uso de maiúscula e underscore.       |
| idade29        | Válido   | Pode conter números (não no início). |
| class          | Inválido | Palavra reservada.                   |
| \_endereco     | Válido   | Começar com underscore é permitido.  |
| 29idade        | Inválido | Não pode começar com número.         |
| nome completo  | Inválido | Espaços não são permitidos; use `_`. |

---

## 🔢 Tipos de Dados

Python é uma linguagem de tipagem dinâmica. Isso significa que você não precisa declarar explicitamente o tipo da variável — ele é definido automaticamente conforme o valor atribuído.

---

### 📋 Tabela de Tipos de Dados

| Tipo    | Descrição                  | Exemplo de Código                       | Exemplo Real                                                  |
| :------ | :------------------------- | :-------------------------------------- | :------------------------------------------------------------ |
| `int`   | Números inteiros.          | `idade = 30`                            | Idade de uma pessoa.                                          |
| `float` | Números com decimais.      | `altura = 1.75`                         | Altura em metros.                                             |
| `str`   | Cadeia de texto.           | `nome = "Carlos"`                       | Nome de alguém.                                               |
| `bool`  | Verdadeiro ou falso.       | `ativo = True`                          | Está ativo?                                                   |
| `list`  | Lista ordenada e mutável.  | `frutas = ["maçã", "banana"]`           | Lista de compras.                                             |
| `tuple` | Lista ordenada e imutável. | `coordenadas = (10, 20)`                | Localização GPS. *(“Tuple” é o termo em inglês para “tupla”)* |
| `dict`  | Estrutura de chave-valor.  | `aluno = {"nome": "Ana", "idade": 20,}` | Cadastro de aluno. |

---

### 📚 Explicação Rápida

- **`int`** → números inteiros.
- **`float`** → números decimais.
- **`str`** → textos (strings).
- **`bool`** → valores lógicos (True ou False).
- **`list`** → coleções mutáveis.
- **`tuple`** → coleções imutáveis.
- **`dict`** → chave e valor (tipo dicionário).

---

## ✅ Exemplo Prático Combinado

```python
nome = "Ana"                           # str
idade = 25                             # int
altura = 1.68                          # float
estudante = True                       # bool
materias = ["Python", "SQL", "Git"]    # list
coordenadas = (34.5, -120.7)           # tuple
perfil = {"nome": "Ana", "idade": 25}  # dict
```

## Comandos de Entrada e Saída

Vamos aprender a interagir com o usuário por meio da entrada (``input``) e saída (``print``) de dados.

---

## 🔹 Saída de Dados: `print()`

O comando `print()` é usado para exibir informações no console.

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

## 🔹 Entrada de Dados: `input()`

O comando `input()` permite receber dados do usuário.

> Exemplo:

```python
nome = input("Digite seu nome: ")
print("Seja bem-vindo(a),", nome)
```

> O programa irá pausar e esperar o usuário digitar algo.
> Tudo o que for digitado será armazenado como string.

## ⚡ Conversão de Tipos (Casting)

Para trabalhar com números, precisamos converter a entrada manualmente usando funções de casting:

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

- **int() :** converte para inteiro.
- **float() :** converte para ponto flutuante.
- **str() :** converte para texto (string), se necessário.

---

## 🚀 Conclusão

Esses primeiros passos são fundamentais na sua jornada com a linguagem Python. A partir daqui, você já consegue construir pequenos scripts que recebem dados, processam informações e mostram resultados na tela!

> Continue praticando! Experimente:

- Criar um programa que calcula a média de duas notas;
- Fazer um cadastro simples com nome, idade e cidade;
- Desenvolva um dicionário que possuam nome, idade, situação(estudando: true), e entre outros ;

> 💾 Dica: salve seus testes em um arquivo como exercicios.py para montar sua própria base de estudos!
> Cada pequeno exercício vai te deixar mais confiante e preparado para os próximos módulos — como estruturas condicionais, repetições, funções e muito mais! 💡🐍

**Próximo Módulo: [Fundamentos da Linguagem](../2.%20fundamentos/README.md)**
