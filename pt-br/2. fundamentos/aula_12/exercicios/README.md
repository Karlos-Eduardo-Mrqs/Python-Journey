# 📝 Exercícios Resolvidos — Aula 12 (Módulo 2)

Neste documento estão as soluções dos exercícios propostos sobre funções em Python.
O objetivo é praticar a criação de funções reutilizáveis, recebendo parâmetros e retornando valores.

---

## [🔹 1. Função de Soma](Ex_01.py)

```python
def soma(a, b):
    return a + b

print(soma(5, 3))   # Saída: 8
print(soma(10, 7))  # Saída: 17
```

> 📌 Explicação: a função recebe dois números, soma e retorna o resultado.

---

## [🔹 2. Função de Média](Ex_02.py)

```python
def media(lista):
    return sum(lista) / len(lista)

print(media([5, 7, 9]))     # Saída: 7.0
print(media([10, 20, 30]))  # Saída: 20.0
```

> 📌 Explicação: usamos ``sum()`` para somar os elementos e ``len()`` para dividir pela quantidade.

---

## [🔹 3. Função de Fatorial](Ex_03.py)

```python
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial(5))  # Saída: 120
print(fatorial(7))  # Saída: 5040
```

> 📌 Explicação: o fatorial multiplica todos os números de 1 até n.

---

## [🔹 4. Função de Verificação de Número Primo](Ex_04.py)

```python
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(eh_primo(7))   # Saída: True
print(eh_primo(10))  # Saída: False
```

> 📌 Explicação: um número é primo se for maior que 1 e não tiver divisores além de 1 e ele mesmo.

---

## [🔹 5. Função de Contagem de Caracteres](Ex_05.py)

```python
def contar_caractere(texto, caractere):
    return texto.count(caractere)

print(contar_caractere("banana", "a"))  # Saída: 3
print(contar_caractere("Python", "o"))  # Saída: 1
```

> 📌 Explicação: usamos o método ``count()`` para contar quantas vezes o caractere aparece na string.

**Próximo Capítulo : [O que são funções ?](../../aula_13/13_O_que_sao_funcoes.md)**
