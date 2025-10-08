# 🔢 Loopings Não Contáveis em Python

Os loopings não contáveis são utilizados quando não sabemos previamente quantas vezes um bloco de código precisa ser executado. Em Python, a estrutura principal para esse tipo de repetição é o while.

---

## 🔹 ``while``

A estrutura ``while`` executa repetidamente um bloco de código enquanto a condição for verdadeira.

> ✅ Sintaxe:

```python
while condição:
    # bloco de código
```

> 📌 Exemplo: imprimir números de 1 a 5 usando while

```python

contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

> 💡 Observação: se a condição nunca se tornar falsa, o loop se tornará infinito. Por isso, sempre garanta que algo dentro do loop altere a condição.

---

## 🔹 Controle de fluxo: ``break``, ``continue`` e ``pass``

### 🔸 ``break``

> Sai imediatamente do loop, mesmo que a condição ainda seja verdadeira. Útil para evitar loops infinitos ou quando encontramos uma condição específica de parada.

```python
contador = 0
while True:
    print(contador)
    if contador == 5:
        break
    contador += 1
```

### 🔸 ``continue``

> Pula a iteração atual e volta para a verificação da condição. Não interrompe o loop, apenas ignora o restante do código dentro da iteração atual.

```python
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 != 0:
        continue  # pula números ímpares
    print(contador)  # imprime apenas números pares
```

### 🔸 ``pass``

> Funciona como um marcador de posição. Não altera o fluxo do loop; é útil para deixar trechos de código “abertos” durante o desenvolvimento.

```python
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        pass  # não faz nada
    print(contador)
```

---

## 🔹 Loopings infinitos

Um loop infinito acontece quando a condição de parada nunca se torna falsa. Loops infinitos podem travar o programa se não forem controlados, mas podem ser úteis em situações como servidores ou programas que aguardam entrada contínua do usuário.

```python
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando.lower() == "sair":
        break  # interrupção do loop infinito
    print(f"Você digitou: {comando}")
```

### 💡 Explicação

1. Esse código cria um loop infinito com while True, que pede ao usuário para digitar algo.
2. Se o usuário digitar "sair" (ou qualquer variação maiúscula/minúscula)
3. o break interrompe o loop, encerrando o programa.
4. Caso contrário, o programa imprime o que foi digitado e volta a pedir outra entrada.

---

## ✅ Conclusão

Loopings não contáveis (``while``) são essenciais quando não sabemos quantas vezes o código deve ser executado.

Combinando ``while`` com ``break``, ``continue`` e ``pass``, conseguimos controlar o fluxo do loop de forma precisa, evitando repetições infinitas e garantindo que o programa se comporte corretamente.

> 🔹 Dica: Sempre revise a condição de parada para evitar loops infinitos.

**Próximo Capítulo : [Funções](../aula_12/12_funcoes.md)**

---

## Exercícios Aula 11

### Contador com while

Imprima os números de 1 a 20 usando while.

### Soma de números até o usuário digitar 0

Leia números do usuário em um loop while e some-os até que seja digitado 0.

### Filtro com continue

Use um loop while para ler números de 1 a 10 e imprimir apenas os múltiplos de 3.

### Interromper com break

Crie um loop que leia números do usuário e pare quando o número for negativo.

### Marcador de pass

Crie um loop que percorra números de 1 a 5 e use pass quando o número for 3.

**[Gabarito](exercicios/README.md)**
