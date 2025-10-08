# 🔹 If, Elif e Else

**A estrutura ``if`` é a base das decisões em Python**. Ela permite que seu programa execute blocos específicos de código apenas quando uma determinada condição é verdadeira. Quando a condição não é satisfeita, o programa pode testar outras condições com ``elif`` ou executar um bloco padrão com ``else``.

> ✅ Sintaxe:

```python
if condição1:
    # bloco de código se condição1 for verdadeira
elif condição2:
    # bloco de código se condição1 for falsa e condição2 for verdadeira
else:
    # bloco de código se todas as condições anteriores forem falsas
```

## Como essa condicional funciona ?

- Bloco ``if``:
  1. Avalia a primeira condição.
  2. Se for verdadeira (``True``), o bloco correspondente é executado e todas as outras condições são ignoradas.
  3. Se for falsa (``False``), o programa passa para o próximo ``elif`` ou para o ``else``.

- Bloco ``elif (opcional)``
  1. Permite testar outras condições caso a condição anterior (if ou outro elif) seja falsa.
  2. Pode ter vários elif em sequência para avaliar várias possibilidades.
  3. **Ele será acionado apenas quando a condição do bloco if for falsa**.

- Bloco ``else (opcional)``
  1. ``É o bloco “catch-all”``, ou seja, executa quando todas as condições anteriores falham.
  2. Ele não possui condição, ou seja, é acionado automaticamente **se nenhuma das condições anteriores for verdadeira.**

### 📌 Exemplo prático: Verificar se um número é positivo, negativo ou zero

```python
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero")
```

#### 🔹 Explicação detalhada

1. ``Se numero > 0``, apenas o primeiro bloco será executado, e os demais são ignorados.
2. ``Se numero < 0``, o primeiro bloco é ignorado, o segundo é executado.
3. ``Se numero não for maior nem menor que zero``, então else cobre todos os casos restantes, garantindo que sempre haja uma resposta.

---

## 🔹 Condicionais Aninhadas

Quando precisamos verificar múltiplas condições dependentes, podemos colocar um if dentro de outro if. Isso é útil para cenários hierárquicos, onde a decisão de um bloco depende de outra condição já avaliada.

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

### Como essa condicional aninhada funciona ?

- Bloco 1º ``if``
  1. Avalia a primeira condição (condição1).
  2. Se for verdadeira (True), executa seu bloco interno e entra no segundo if.
  3. Se for falsa (False), ignora o bloco interno e vai direto para o else correspondente.

- Bloco 2º ``if (dentro do primeiro)``
  1. Avalia a segunda condição (condição2).
  2. Se for verdadeira, executa o bloco interno correspondente.
  3. Se for falsa, executa o bloco do else interno, que cobre apenas o caso em que condição1 é verdadeira e condição2 é falsa.

- Bloco ``else (opcional)``
  1. Serve como “catch-all”, ou seja, é acionado quando a condição do primeiro if é falsa.
  2. Não possui condição própria, executando automaticamente quando nenhuma das condições anteriores é satisfeita.

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

#### 🔹 Explicação detalhada da condição aninhada

1. O programa primeiro avalia se a nota é suficiente (``>= 7``).
2. Se a nota for adequada, ele entra no segundo nível de verificação: a frequência.
3. Se ambos os critérios forem atendidos, o aluno é aprovado.
4. Se apenas a nota estiver ok, mas a frequência não, o aluno é reprovado por frequência.
5. Se a nota não atingir o mínimo, o programa ignora a verificação da frequência e imprime reprovado por nota.

---

## 🚀 Conclusão

As estruturas condicionais em Python permitem que seu programa tome decisões de forma inteligente, executando blocos de código diferentes de acordo com as condições avaliadas. Neste capítulo, você aprendeu:

1. ``if, elif e else:`` a base para criar decisões lineares, avaliando condições simples ou múltiplas de forma sequencial.

2. ``Condicionais aninhadas:`` como criar decisões hierárquicas, onde uma condição depende do resultado de outra, permitindo cenários mais complexos e precisos.

3. Bloco ``else`` como ``catch-all``: sempre garante que exista um caminho padrão caso nenhuma condição seja satisfeita, evitando falhas no programa.

> Com esses conceitos, você agora consegue criar programas que se adaptam a diferentes cenários, validam dados e garantem respostas corretas de acordo com a lógica definida.

**Próximo Capítulo: [Condicionais com Match Case e Operador Ternário](../aula_08/08_condicionais_match_case_ternario.md)**

---

## 📝 Exercícios Aula 07

### Verificação de senha

1. Crie um programa que peça a senha do usuário.
2. Se a senha for ``"python123"``, exiba ``"Acesso permitido"``.
3. Caso contrário, exiba ``"Acesso negado"``.

### Velocidade permitida

1. Implemente um programa que leia a velocidade de um carro.
2. Se for até ``80 km/h``, exiba ``"Dentro do limite"``.
3. Se for maior, calcule a multa de ``R$5,00 por km acima do limite`` e mostre o valor.

### Adivinhação de número

1. Crie um programa que leia um número digitado pelo usuário e compare com um número secreto definido no código.
2. Se o usuário acertar, exiba ``"Você acertou!"``.
3. Caso contrário, diga se o número é maior ou menor que o secreto.

### Ano Bissexto

1. Faça um programa que leia um ano
2. Verifique se ele é bissexto ou não bissexto.
3. Um ano é bissexto se for divisível por 4.
4. Não é divisível por 100, exceto se também for divisível por 400.

**[Gabarito](exercicios/README.md)**
