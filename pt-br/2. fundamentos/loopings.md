# ⚙️ Estruturas de Repetição em Python

As estruturas de repetição permitem que um bloco de código seja executado várias vezes, com base em uma condição ou em um número específico de iterações. Elas são essenciais para automatizar tarefas repetitivas e processar grandes volumes de dados de forma eficiente.

## 📌 Por que são importantes?

- Permitem automatizar tarefas repetitivas;
- Facilitam o processamento de coleções de dados;
- Tornam o código mais compacto e fácil de entender;

## 🔷 Principais tipos de repetição

### 🔹 for

A estrutura for é usada para iterar sobre uma sequência (como uma lista, tupla, string ou intervalo de números). Ele é ideal para quando você sabe o número de iterações que deseja realizar.

> ✅ Sintaxe:

```python
for item in sequencia:
    # bloco de código
```

> 📌 Exemplo de uso: Iterar sobre uma lista de números e imprimir cada um.

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

### 🔷 while

A estrutura while executa um bloco de código enquanto uma condição for verdadeira. É útil quando o número de iterações não é conhecido de antemão.

> ✅ Sintaxe:

```python
while condição:
    # bloco de código
```

> 📌 Exemplo de uso: Imprimir números de 1 a 5 com while.

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

## 🔹 break, continue e pass

Essas instruções alteram o comportamento padrão de loops como for e while.

### 🔸 break

A instrução break é usada para interromper um loop prematuramente. Quando o Python encontra um break, ele sai imediatamente do laço e continua a execução do código após o laço.

> 📌 Exemplo de uso com break:

```python
numero = 0
for numero in range(10):
    print(numero) #  0, 1 , 2 , 3 , 4 , 5
    if numero == 5: 
        break  # Interrompe o loop quando o número for 5
    print(numero)
```

### 🔸 continue

A instrução continue faz com que o loop pule a iteração atual e vá diretamente para a próxima iteração, sem executar o restante do código dentro do loop para a iteração atual.

> 📌 Exemplo de uso com continue:

```python
numero =  0
for numero in range(10):
    print(numero) # 0 , 1 , 2 , 3 , 4 , 6 , 7 , 8, 9
    if numero == 5:
        continue  # Pula a iteração quando o número for 5
    print(numero)

```

### 🔸 pass

A instrução pass é um marcador de lugar. Ela é útil quando você precisa de uma estrutura de controle, como um if ou um loop, mas não deseja que nada aconteça dentro dessa estrutura, ou ainda, se você está desenvolvendo o código e quer deixar uma parte em aberto sem erros.

> 📌 Exemplo de uso com pass:

```python
numero =  0
for numero in range(5):
    print(numero) # 0 , 1 , 2 , 3 , 4 
    if numero == 3:
        pass  # Não faz nada quando o número for 3
    print(numero)
```

## 🔷 Funções de iteração

### 🔹 range()

A função range() é usada para gerar uma sequência de números, muito útil em loops for. Ela pode receber até três argumentos: start, stop e step.

> ✅ Sintaxe:

```python
start:1 # valor inicial (inclusivo).
stop: 10 # valor final (exclusivo).
step: 1 # valor do incremento (opcional).

range(start, stop, step)
```

> 📌 Exemplo de uso com range(): Criar uma sequência de números de 0 a 9.

```python
for i in range(10):
    print(i)
📌 Exemplo de uso com range(): Criar uma sequência com um incremento de 2.
```

```python
for i in range(0, 10, 2):
    print(i)
```

### 🔹 enumerate()

A função enumerate() adiciona um contador automático a um iterável, retornando uma tupla com o índice e o valor.

> ✅ Sintaxe:

```python
enumerate(iterable)
```

> 📌 Exemplo de uso com enumerate(): Iterar sobre uma lista e obter o índice e o valor.

```python
frutas = ["maçã", "banana", "cereja"]
for index, fruta in enumerate(frutas):
    print(f"Índice {index}: {fruta}")
```

### 🔹 zip()

A função zip() combina dois ou mais iteráveis, retornando uma sequência de tuplas. Cada tupla contém os elementos correspondentes dos iteráveis.

> ✅ Sintaxe:

```python
zip(iterable1, iterable2, ...)
```

> 📌 Exemplo de uso com zip(): Combinar duas listas e iterar sobre elas.

```python
nomes = ["João", "Maria", "Carlos"]
idades = [25, 30, 22]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")
```

### 🔹 Compreensão de Listas (List Comprehensions)

A compreensão de listas oferece uma forma compacta e eficiente de criar listas a partir de outras coleções ou sequências, usando uma sintaxe mais simples do que os loops tradicionais. Além disso , é especialmente útil quando você deseja aplicar uma transformação simples a cada elemento de uma lista ou filtrá-los com uma condição.

> ✅ Sintaxe:

```python
[expressao for item in iteravel if condicao]
```

> 📌 Exemplo de uso:

```python
numeros = [1, 2, 3, 4, 5]
quadrados = [numero**2 for numero in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```