# 🔹 Operador Ternário

O operador ternário permite escrever condições simples em uma única linha, o que torna o código mais enxuto e elegante.
Ele é útil principalmente quando precisamos atribuir um valor a uma variável com base em uma condição, sem precisar usar múltiplas linhas de ``if/else``.

> ✅ Sintaxe:

```python
valor_se_verdadeiro if condicao else valor_se_falso 
```

> 📌 Exemplo de uso:

```python
status = "Aprovado" if nota >= 7 else "Reprovado" # Se a nota for maior ou igual a sete, o status será aprovado, caso contrário, o status será reprovado
```

## Explicação detalhada do exemplo

1. O Python primeiro avalia a condição (``nota >= 7``).
2. Se for ``True``, retorna o valor antes do ``if`` (``"Aprovado"``).
3. Se for ``False``, retorna o valor depois do ``else`` (``"Reprovado"``).

### 💡 Boas práticas do ternário

1. Use ternário apenas para condições simples, evitando encadeamentos complexos que dificultem a leitura.
2. Ideal para atribuições de variáveis ou pequenas decisões em expressões.
3. Para múltiplas condições, prefira o ``if/elif/else`` tradicional, que mantém o código mais claro.

---

## 🔹 Match case (válido na versão Python 3.10+)

O match case é uma estrutura poderosa que substitui o switch de outras linguagens. Ele permite comparar uma variável com múltiplos valores possíveis, executando blocos de código específicos para cada caso.

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

### Explicação detalhada do código

1. O Python avalia a variável após ``match`` (cor).
2. Compara com cada ``case`` na ordem em que aparecem.
3. Executa apenas o bloco do primeiro case que corresponder.
4. O ``case _`` funciona como um ``catch-all``, sendo executado se nenhum dos valores anteriores corresponder.

#### 💡 Vantagens do match case

1. Torna o código mais legível do que múltiplos ``elif``.
2. Permite comparar valores literais, padrões e até tipos complexos.
3. Útil em cenários como menus, comandos de usuário ou classificação de dados.

> ⚠️ Observação: O match case está disponível apenas em Python 3.10 ou superior.

---

## 🚀 Conclusão

Neste capítulo, você aprendeu duas formas avançadas de lidar com decisões em Python, além do ``if/elif/else`` tradicional:

- **Operador Ternário**
  1. Permite escrever condições simples em uma única linha, tornando o código mais enxuto e elegante.
  2. Ideal para atribuições rápidas de variáveis ou decisões diretas.
  3. Deve ser usado apenas para casos simples, evitando aninhamentos complexos que dificultem a leitura.

- **Match Case (Python 3.10+)**
  1. Estrutura poderosa para comparar uma variável com múltiplos casos, substituindo longos encadeamentos de ``elif``.
  2. O ``case _`` funciona como um catch-all, garantindo que sempre haja um bloco de fallback.
  3. Facilita a leitura e manutenção do código, especialmente em menus, comandos e classificações de dados.

**Próximo Capítulo: [Loopings](../aula_09/09_loopings.md)**

---

## 📝 Exercícios de Condicionais

### Mês do ano (com match case)

1. Faça um programa que leia ``um número de 1 a 12`` e informe o mês correspondente usando match case.
2. Exemplo:``1 → Janeiro, 2 → Fevereiro, etc.``
3. Caso o número não esteja no intervalo, exiba ``"Mês inválido"``.

### Maioridade com operador ternário

1. Faça um programa que leia a idade de uma pessoa e diga:
2. ``"Maior de idade"`` se for 18 anos ou mais,
3. ``"Menor de idade"`` caso contrário.

### Sistema de Notas com condicionais

1. Implemente um programa que leia uma letra de conceito (``A, B, C, D, E ou F``) e use match case para exibir a mensagem correspondente:
2. Categorias das notas:
3. ``A → "Excelente"``;
4. ``B → "Bom"``;
5. ``C → "Regular"``;
6. ``D → "Ruim"``;
7. ``D → "Muito Ruim"``;
8. ``F → "Reprovado"``;
9. ``Outro valor → "Conceito inválido"``;

### Categoria de IMC

1. Crie um programa que leia o peso e a altura de uma pessoa e calcule o IMC.
2. Classifique de acordo com a tabela:
3. ``Menor que 18.5 → Abaixo do peso;``
4. ``Entre 18.5 e 24.9 → Peso normal;``
5. ``Entre 25.0 e 29.9 → Sobrepeso;``
6. ``30.0 ou mais → Obesidade;``

**[Gabarito](exercicios/README.md)**
