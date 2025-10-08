# 🔢 Operadores em Python

Operadores são **símbolos especiais** usados para realizar operações em variáveis e valores.  
Eles são fundamentais em qualquer linguagem de programação, pois permitem:  

- 📊 Executar cálculos matemáticos  
- ⚖️ Comparar valores  
- 🧠 Tomar decisões lógicas  
- 🔍 Verificar pertencimento e identidade  

> **Em Python, os operadores são classificados em diferentes grupos, cada um com sua função.**  

---

## 📚 Estrutura de estudo dos operadores

Para facilitar o aprendizado, vamos dividir os operadores em blocos de afinidade:

### [🧮 1. Operadores de Cálculo](../aula_02/02_operadores_calculo.md)

Incluem três categorias que trabalham diretamente com **números e valores**:

- **Aritméticos** → `+`, `-`, `*`, `/`, `//`, `%`, `**`  
- **Atribuição** → `=`, `+=`, `-=`, `*=`, `/=`, etc.  
- **Bit a Bit (Bitwise)** → ``&``, ``|``, ``^``, ``~``, ``<<``, ``>>``

> 👉 São os operadores que usamos para **calcular e manipular valores numéricos**.  

---

### [⚖️ 2. Operadores Condicionais](../aula_03/03_operadores_condicionais.md)

Aqui entram os operadores usados em **decisões e comparações**:

- **Relacionais (comparação)** → `==`, `!=`, `>`, `<`, `>=`, `<=`  
- **Lógicos** → `and`, `or`, `not`  

> 👉 São fundamentais para **estruturas condicionais** (ex: `if`, `while`).  
> 👉 Também veremos a **Tabela Verdade**, que mostra como os operadores lógicos funcionam.  

---

### [🔍 3. Operadores de Verificação](../aula_04/04_operadores_verificacao.md)

Servem para verificar **pertencimento** ou **identidade de objetos**:

- **Membros** → `in`, `not in`  
- **Identidade** → `is`, `is not`  

> 👉 Muito usados em **coleções** (listas, tuplas, dicionários) e em **comparações entre objetos**.  

---

### [📑 4. Resumo e Precedência](../aula_05/05_resumo_operadores.md)

Por fim, vamos revisar tudo e entender a **ordem de execução dos operadores** em Python.  
Isso é importante porque, em expressões mais complexas, a precedência define **quem é executado primeiro**.  

Exemplo:  

```python
resultado = 2 + 3 * 4
print(resultado)  # Saída: 14 ou 20 ?
```

---

## 🚀 Conclusão

Os operadores em Python são ferramentas essenciais para realizar operações e comparar dados de forma eficiente. A partir dessa visão geral, você pode realizar desde simples cálculos aritméticos até manipulação avançada de dados com operadores lógicos, bit a bit e de atribuição.

**💡 Próximos Passos:** Depois de dominar os operadores, explore como utilizá-los em estruturas condicionais e estruturas de repetição. Isso vai permitir que você escreva programas mais dinâmicos e interessantes!

> Obs. : Veja todos os capítulos sobre os operadores antes de ver o próximo capítulo Condicionais.

**Próximo Capítulo : [Condicionais](../aula_06/06_condicionais.md)**

---

## 📝 Exercícios Aula 01 — Módulo 2

- *Operadores Aritméticos:* Crie um programa que faça as quatro operações matemáticas com números fornecidos pelo usuário

- *Operadores Relacionais:* Desenvolva um sistema que compare a idade de duas pessoas e diga quem é mais velho.

- *Operadores Lógicos:* Verifique se um número está entre dois valores (usando ``and`` e ``or``).

- *Operadores de Membros:* Crie um programa que pergunte ao usuário por um item e verifique se esse item está em uma
lista de compras.

- *Operadores Bit a Bit:* Experimente manipular os bits de um número e veja como ele altera o valor.

**🔍 Dica:** A prática constante é a chave para solidificar o entendimento dos operadores. Com o tempo, eles se tornarão naturais no seu código!

> Dominar os operadores te dá controle total sobre como seu programa toma decisões e transforma dados. Essa é a base para criar sistemas inteligentes e eficientes!

**[Gabarito dos exercícios](exercicios/README.md)**
