# 📝 Exercícios da Aula 03 — Módulo 1

Este documento contém os exercícios práticos do Módulo 1 dentro da Aula 03, com soluções comentadas.

O objetivo é reforçar conceitos iniciais de variáveis, tipos de dados, entrada/saída e estruturas básicas.

---

## Exercício 01 — Calculando a média de duas notas

**Objetivo:** Praticar operações matemáticas simples e entrada de dados.

### [1ª Opção **(valores atribuídos diretamente)**](Ex_01_pt1.py)

```python
nota_1, nota_2 = 7.5 , 8.0 

media = (nota_1 + nota_2) / 2 
print("Media = ",media)
```

### [2ª Opção **(valores digitados pelo usuário)**](Ex_01_pt2.py)

```python
nota_1 = float(input("Digite a primeira nota do aluno:"))
nota_2 = float(input("Digite a segunda nota do aluno:"))

media = (nota_1 + nota_2)/2

print("Media = ", media)
```

**Explicação:**
Na primeira versão, as notas já estão definidas. Na segunda, o programa pede ao usuário que as insira. Em ambos os casos, a média é calculada pela soma das notas dividida por 2.

---

### [Exercício 02 — Cadastro simples de usuário](Ex_02.py)

**Objetivo:** Coletar e exibir informações do usuário.

```python
nome = input("Digite o seu nome usuário:")
idade = int(input("Digite a sua idade usuário:"))
cidade = input("Digite a sigla ou nome da sua cidade:")

print("Cadastro sucedido ! ")
print("Nome:",nome," Idade:",idade," Cidade:",cidade)
```

**Explicação:**
A função ``input()`` captura o nome e a cidade como strings. A idade é convertida para inteiro com ``int()``. Em seguida, os dados são exibidos de forma organizada, simulando um cadastro básico.

---

### [Exercício 03 — Cadastro usando dicionário](Ex_03.py)

**Objetivo:** Introduzir dicionários como forma de armazenar dados relacionados.

```python
aluno = {
    "nome":"Leonardo_Queiroz",
    "idade": 24,
    "estudando": True,
    "dirige":False
}

print(aluno)
```

**Explicação:**
O dicionário armazena pares chave: valor, facilitando a organização de informações. Aqui, ``o dicionário aluno`` **guarda nome, idade, se estuda e se dirige**. Com ``print(aluno)``, todos os dados são exibidos de forma compacta.

> 💡 Dica: Esses exercícios ajudam a consolidar conceitos básicos de Python, como variáveis, tipos de dados, entrada de dados e estruturas de armazenamento simples (dicionários). Praticar cada um deles fortalece a base para módulos mais avançados.

**Próximo Capítulo : [📘 Fundamentos do Python](../../../2.%20fundamentos/README.md)**
