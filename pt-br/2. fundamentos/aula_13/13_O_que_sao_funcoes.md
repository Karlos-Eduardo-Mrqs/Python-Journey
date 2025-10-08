# ✨ O que são funções?

Funções são blocos de código que agrupam instruções para realizar uma tarefa específica. Elas podem ser chamadas em diferentes partes do programa sempre que for necessário executar essa tarefa.

> ➡️ Em vez de repetir o mesmo código várias vezes, você o escreve apenas uma vez dentro de uma função e o reutiliza quando precisar.

## 🔎 Por que usar funções?

- *Organização* → deixam o código dividido em partes menores, mais fáceis de entender.
- *Reutilização* → você escreve uma vez e usa várias vezes.
- *Legibilidade* → facilitam a leitura e manutenção do programa.
- *Escalabilidade* → programas grandes ficam mais fáceis de expandir.

---

## 🖥️ Exemplo simples: Saudação()

```python
def saudacao():
    print("Olá, seja bem-vindo(a)!")
```

> ➡️ Neste exemplo, criamos uma função chamada ``saudacao``. Sempre que chamarmos ``saudacao()``, a mensagem será exibida.

### ▶️ Chamando a função

```python
# Chamando a função criada
saudacao()
saudacao()
```

> 🔑 Perceba como podemos reutilizar o mesmo bloco de código várias vezes sem precisar reescrevê-lo.

---

## 🚀 Exemplos práticos

- *Função de boas-vindas personalizada:*

```python
def boas_vindas():
    print("Bem-vindo ao sistema Python Journey!")
    print("Esperamos que aproveite o aprendizado.")
    
boas_vindas()
```

- *Demonstrando reutilização:*

```python
def linha():
    print("-" * 30)

print("Início do programa")
linha()
print("Processando dados...")
linha()
print("Fim do programa")
```

---

## 📌 Conclusão

As funções representam um dos principais recursos da programação, pois permitem organizar, reutilizar e simplificar o código.
Com elas, você consegue dividir programas em partes menores e mais claras, facilitando tanto o aprendizado quanto a manutenção.

> 👉 Esse capítulo fecha com a primeira noção de funções: blocos de código reutilizáveis.
> > Nos próximos, vamos ver como passar informações para dentro das funções usando parâmetros e como controlar seus retornos.

**Próximo Capítulo: [Declaração e Chamadas de Funções](../aula_14/14_declaracao_de_funcoes.md)**

---

## 📝 Exercícios Aula 13

### Crie uma função chamada ``apresentacao()`` que exiba seu nome e curso

### Crie uma função ``menu()`` que imprima uma lista de opções (ex: 1 - Início, 2 - Ajuda, 3 - Sair)

### Escreva uma função chamada ``separador()`` que imprima uma linha de = para organizar a saída

**[Gabarito](exercicios/README.md)**
