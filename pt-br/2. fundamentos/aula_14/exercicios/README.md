# 📝 Exercícios Resolvidos — Aula 14 (Módulo 2)

Nesta aula, trabalhamos declaração de funções com def, chamadas de funções e a diferença entre argumentos posicionais e nomeados.

---

## [🔹 1. Função Dobro](Ex_01.py)

```python
def dobro(numero):
    print(f"O dobro de {numero} é {numero * 2}")

dobro(5)
dobro(7)
```

> 📌 Explicação: A função ``dobro()`` recebe um número e imprime seu dobro. Mostra como funções podem receber parâmetros e executar operações simples.

---

## [🔹 2. Função Revelar Dados](Ex_02.py)

```python
def revelar_dados(nome, cidade, idade):
    print(f"Nome: {nome} | Idade: {idade} | Cidade: {cidade}")

revelar_dados("Ana", 22, "São Paulo")
revelar_dados("Eduardo", 20, "Porto Alegre")
```

> 📌 Explicação: Função com três parâmetros, mostrando como exibir informações organizadas. Reutilizável para qualquer pessoa.

---

## [🔹 3. Função Calcular Média](Ex_03.py)

```python
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A média das notas é: {media:.1f}")

calcular_media(8, 7)
calcular_media(10, 9.5)
```

> 📌 Explicação: Função que recebe duas notas, calcula a média e formata a saída com uma casa decimal.

---

## [🔹 4. Função Produto (Argumentos Posicionais e Nomeados)](Ex_04.py)

```python
def produto(nome, preco, quantidade):
    print(f"Produto: {nome} | Preço: {preco} | Quantidade: {quantidade}")

# Argumentos posicionais
produto("Caderno", 15.5, 3)

# Argumentos nomeados (ordem trocada)
produto(quantidade=2, nome="Caneta", preco=2.75)
```

> 📌 Explicação: **Posicionais:** respeitam a ordem dos parâmetros definidos. **Nomeados:** permitem alterar a ordem, desde que especifiquemos a qual parâmetro o valor pertence.

**Próximo Capítulo : [Parametros Escopos](../../aula_15/15_parametros_escopo.md)**
