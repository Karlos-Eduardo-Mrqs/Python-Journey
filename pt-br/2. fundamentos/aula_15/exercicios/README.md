# 📝 Exercícios Resolvidos — Aula 15 (Módulo 2)

Nesta aula, exploramos parâmetros opcionais, retornos de valores e escopo de variáveis em Python.

---

## [🔹 1. Estatísticas de uma Lista](Ex_01.py)

```python
def estatisticas(lista_num):
    media_lista_num = sum(lista_num) / len(lista_num)
    print(f"Maior Número: {max(lista_num)} | Menor Número: {min(lista_num)} | Média: {media_lista_num:.2f}")

estatisticas([5,6,7,8,12,9,15,8,13,4,2,1])
```

> 📌 Explicação: Calcula média, maior e menor valor de uma lista. Demonstra como usar parâmetros de função e funções embutidas (``sum, max, min``). **Escopo local:** media_lista_num existe apenas dentro da função.

---

## [🔹 2. Compra com Valor Local](Ex_02.py)

```python
def comprar(valor):
    valor_local = 500
    print(f"Valor da variável local: {valor_local}")
    return valor_local - valor

valor_usuario = 150.45
print(f"Valor usuário {valor_usuario:.2f} X Valor local {comprar(valor_usuario)}")
```

> 📌 Explicação: ``valor_local`` é uma variável local, acessível apenas dentro da função comprar. A função retorna um valor que pode ser usado fora do escopo da função. Demonstra como funções podem processar informações e devolver resultados.

---

## [🔹 3. Verificação de Idade](Ex_03.py)

```python
def verificar_idade(idade):
    classifica_idade = {
        "Menor de idade !": idade < 18, 
        "Maior de idade !": idade >= 18
    }
    for mensagem, valor_verdadeiro in classifica_idade.items():
        if valor_verdadeiro:
            print(f"Se você tem {idade} anos, então você é {mensagem}")

verificar_idade(20)
verificar_idade(18)
verificar_idade(30)
verificar_idade(14)
```

> 📌 Explicação: Cria um dicionário de condições e verifica qual é verdadeira. Demonstra uso de escopo local (classifica_idade existe apenas dentro da função). Ensina a combinar estruturas de decisão com funções.

**Próximo Capítulo : [Funções Lambda](../../aula_16/16_funcoes_lambda.md)**
