# ⚙️ Condicionais em Python

As estruturas condicionais permitem que seu código tome decisões com base em condições específicas. Elas tornam seu programa mais dinâmico, flexível e adaptável às diferentes entradas e situações. Com condicionais, você pode:

- **✅ Verificar valores e executar comandos específicos**
- **✅ Definir fluxos de execução diferentes**
- **✅ Criar validações e tratamento de dados**
- **✅ Melhorar a lógica e a dinâmica do programa**

> **Em Python, **as condicionais são utilizadas com operadores relacionais, lógicos e outras ferramentas de decisão.**

---

## 📚 Estrutura de estudo das condicionais

Para facilitar o aprendizado, vamos dividir as condicionais em blocos de afinidade:

### [🔹 1. If, Elif, Else e Condicionais Aninhadas](../aula_07/07_condicionais_aninhadas.md)

A estrutura básica de decisão em Python. Permite executar diferentes blocos de código conforme condições e combinações de decisões aninhadas.

> 👉 Inclui if, elif, else e condicionais dentro de outras condicionais para cenários hierárquicos.

**Exemplos de uso:**

- Verificar se um número é ``positivo``, ``negativo`` ou ``zero``
- Avaliar notas considerando múltiplos critérios (``nota`` e ``frequência``)

---

### [🔹 2. Operador Ternário e Match Case (Python 3.10+)](../aula_08/08_condicionais_match_case_ternario.md)

Ferramentas avançadas para decisões mais compactas e estruturadas:

**Operador ternário**: expressão condicional de uma linha

**Match case**: múltiplos casos baseados em um valor, similar ao switch de outras linguagens

> 👉 Perfeito para simplificar decisões curtas ou múltiplos cenários de maneira legível.

**Exemplos de uso:**

- Atribuir status de aprovação usando uma linha com ternário
- Escolher ação com base em uma variável usando match case

---

## 🚀 Conclusão

As estruturas condicionais em Python são ferramentas poderosas que permitem ao seu código tomar decisões com base em condições dinâmicas.

Elas são essenciais para controlar o fluxo do programa, tornando-o flexível e adaptável às diferentes entradas e situações. Ao entender como usar o ``if, elif, else``, as condicionais aninhadas, o operador ternário e o match case, você terá um conjunto robusto para lidar com qualquer tipo de situação condicional.

## 🔧 Dicas para a prática

- **Validação de entradas de usuário:**
Use condicionais para validar entradas de dados, como cálculos de descontos baseados em idade ou categoria de cliente.

- **Múltiplos casos:**
Utilize o match case para sistemas que envolvem múltiplos casos, tornando seu código mais organizado e legível.

> Obs. : Veja todos os capítulos sobre as condicionais antes de ver o próximo capítulo Loopings.

**Próximo Capítulo : [Loopings](../aula_09/09_loopings.md)**

---

## 📝 Exercícios de Condicionais

### Verificar se o número é positivo, negativo ou zero

1. Implemente um programa que leia um número.
2. Imprima se ele é positivo, negativo ou zero.

### Classificação de idades

1. Crie um programa que leia a idade de uma pessoa e classifique-a como:
2. Criança (``0 a 12 anos``)
3. Adolescente (``13 a 17 anos``)
4. Adulto (``18 a 64 anos``)
5. Idoso (``65 anos ou mais``)

### Verificação de notas

1. Faça um programa que leia uma nota de 0 a 10 e informe se o aluno foi aprovado, reprovado ou se está de recuperação. O critério é:
2. Aprovado: ``nota >= 7``;
3. Recuperação: ``5 <= ou nota < 7``;
4. Reprovado: ``nota < 5``;

### Calculadora simples

1. Crie um programa que leia dois números
2. Digite um operador matemático (``+, -, *, /``).
3. O programa deve executar a operação correspondente entre os dois números e mostrar o resultado.

### Maior de três números

1. Crie um programa que leia três números.
2. imprima o maior número entre eles, utilizando estruturas condicionais.

**[Gabarito](exercicios/README.md)**
