# ⚙️ Estruturas Condicionais em Python

As estruturas condicionais permitem que seu código tome decisões com base em condições específicas. Dessa forma, você pode criar programas que se comportam de maneira diferente de acordo com as entradas e situações.

## 📌 Por que são importantes?

- Verificar valores e executar comandos específicos;
- Definir fluxos de execução diferentes;
- Criar validações e tratamento de dados;
- Melhorar a lógica e dinâmica do programa;

## 🔷 Principais tipos de condicionais:

### 🔹 if, elif e else

A estrutura mais básica e comum para tomar decisões em Python. Permite executar blocos diferentes de código com base em uma ou mais condições.

> ✅ Sintaxe:

```python
if condição1:
    # bloco de código se condição1 for verdadeira
elif condição2:
    # bloco de código se condição1 for falsa e condição2 for verdadeira
else:
    # bloco de código se todas as condições anteriores forem falsas
```

> 📌 Exemplo de uso: Verificar se um número é positivo, negativo ou zero.

```python
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero")
```

### 🔹 Condicionais Aninhadas

São estruturas if dentro de outras estruturas if. Permitem verificar condições dependentes ou hierárquicas, aprofundando a lógica de decisão.

> ✅ Sintaxe:

```python
if condição1:
    if condição2:
        # bloco se ambas as condições forem verdadeiras
    else:
        # bloco se condição1 for verdadeira e condição2 for falsa
else:
    # bloco se condição1 for falsa
```

> 📌 Exemplo de uso: Validar duas condições encadeadas, como nota e presença.

```python
if nota >= 7:  # Se a nota for maior ou igual a sete, avance no algoritmo
    if frequencia >= 75:  # Se a frequência for maior ou igual a 75%, será aprovado
        print("Aprovado")
    else:
        print("Reprovado por frequência")
else:
    print("Reprovado por nota")
```

### 🔹 Operador Ternário

Uma forma compacta de escrever condições simples em uma única linha. Ideal quando você quer atribuir valores ou retornar expressões curtas de forma elegante.

> ✅ Sintaxe:

```python
valor_se_verdadeiro if condicao else valor_se_falso 
```

> 📌 Exemplo de uso:

```python
status = "Aprovado" if nota >= 7 else "Reprovado" # Se a nota for maior ou igual a sete, o status será aprovado, caso contrário, o status será reprovado
```

### 🔹 Match case (válido na versão Python 3.10+)

É a estrutura introduzida no Python 3.10 para substituir o switch de outras linguagens. Permite comparar um valor com múltiplos "casos", tornando o código mais limpo e organizado para múltiplas decisões baseadas em um mesmo valor.

> ✅ Sintaxe:

```python
match variavel:
    case valor1:
        # bloco de código para valor1
    case valor2:
        # bloco de código para valor2
    case _:
        # bloco padrão (equivalente ao "default")
```

> O caractere _ (underscore) representa o caso "padrão", que será executado se nenhum dos anteriores for satisfeito.

> 📌 Exemplo de uso:

```python
cor = "vermelho"

match cor:
    case "vermelho":
        print("Cor escolhida: Vermelho")
    case "azul":
        print("Cor escolhida: Azul")
    case "verde":
        print("Cor escolhida: Verde")
    case _:
        print("Cor não reconhecida")
```