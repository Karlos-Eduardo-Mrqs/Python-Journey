# Exercícios de Dicionários em Python — Aula 03 (Módulo 3)

Este projeto contém a resolução de exercícios de dicionários em Python, abordando manipulação de registros, cálculo de médias e gerenciamento de contatos. Abaixo está uma explicação detalhada de cada exercício e do código utilizado.

---

## [🔹 1. Listando e atualizando funcionários](EX_01.py)

```py
def listar_funcionarios(dicionario:dict,status_titulo:str):
    print("------------------------------------")
    print(status_titulo)
    for id,info in dicionario.items():
        print(f"Id : {id} | Nome : {info['nome']} | Salário : {info['salario']:.2f}")
    print("------------------------------------")

dicionarios_funcionarios = {
    1: {"nome":"Lucas Andrade","idade":20,"salario":1564.20},
    2: {"nome":"Gabriel Morais","idade":22,"salario":1445.60},
    3: {"nome":"Victor Leon","idade":25,"salario":1321.80},
    4: {"nome":"?????","idade":0,"salario":1200.00},
}

listar_funcionarios(dicionarios_funcionarios,"Lista original sem alterações")

dicionarios_funcionarios[3]['salario'] = 1562.70
dicionarios_funcionarios.pop(4)

listar_funcionarios(dicionarios_funcionarios,"Lista atualizada")
```

> Explicação:

1. ``dicionarios_funcionarios`` é um dicionário de dicionários, onde cada funcionário tem id, nome, idade e salario.

2. listar_funcionarios percorre o dicionário com for id, info in dicionario.items() e exibe cada registro.

3. ``dicionarios_funcionarios[3]['salario'] = 1562.70`` atualiza o salário do funcionário com id=3.

4. ``dicionarios_funcionarios.pop(4)`` remove o funcionário com ``id=4``.

5. As chamadas da função antes e depois das alterações mostram a lista original e a lista atualizada.

---

## [🔹 2. Calculando média de alunos e listando os que estão acima](EX_02.py)

```py
def media_turma(dicionario:dict) -> float:
    notas = [aluno['nota'] for aluno in dicionario.values()]
    return sum(notas) / len(notas)

def listar_alunos_media_alta(dicionario:dict,media:float):
    print("Alunos acima da média:")
    for id,aluno in dicionario.items():
        if aluno["nota"] > media:
            print(f"Id: {id} | Nome : {aluno['nome']}")

dicionario_alunos = {
    1: {"nome":"Pedro Fonseca","nota":9.5},
    2: {"nome":"Yan Sacramento","nota":10.0},
    3: {"nome":"João Macedo","nota":8.5},
    4: {"nome":"Miguel Santos","nota":7.5},
    5: {"nome":"Caua Souza","nota":8.5}, 
    6: {"nome":"Victor Goldman","nota":10.0}, 
}

media = media_turma(dicionario_alunos)
print(f"A média da turma é {media:.1f}")

dicionario_alunos[5]["nota"] = 9.4
listar_alunos_media_alta(dicionario_alunos,media)
```

> Explicação:

1. ``media_turma`` cria uma lista com todas as notas usando list comprehension e calcula a média.
2. ``listar_alunos_media_alta`` percorre os alunos e imprime aqueles com nota maior que a média.
3. ``dicionario_alunos[5]["nota"] = 9.4`` atualiza a nota do aluno com ``id=5``.
4. A função lista corretamente os alunos que ficaram acima da média, considerando a nota atualizada.

---

## [🔹 3. Gerenciamento de contatos](EX_03.py)

```py
def adicionar_novo_contato(dicionario: dict,nome:str,telefone:str,email:str):
    if dicionario: 
        id_contato = max(dicionario.keys()) + 1
        dicionario[id_contato] = {"nome":nome,"telefone":telefone,"email":email}
        print("Contato adicionado com sucesso !")
    else:
        print("Você não especificou qual é o dicionário !")

def remover_contato(dicionario:dict,id:int,nome:str):
    if dicionario: 
        mensagem_apagar =  str(input(f"Desejar apagar o contato {nome} ? [S - sim | N - não] :")).strip().upper()
        if mensagem_apagar == "S" and id in dicionario: 
            dicionario.pop(id)
            print("Contato foi removido com sucesso !")
        else:
            print("O código de identificação(id) não existe !")
    else:
        print("Você não especificou qual é o dicionário !")

def listar_contatos(dicionario:dict):
    if dicionario: 
        print("Listando contatos:")
        for id,contato in dicionario.items():
            print(f"|ID -> {id} | Nome : {contato['nome']} | Telefone : {contato['telefone']} | E-mail: {contato['email']} |")
    else:
        print("Você não especificou qual é o dicionário !")

dicionario_contatos = {
    1: {"nome":"Lucas Moura", "telefone":"21-07889223", "email":"LucasMoura@gmail.com"}
}

adicionar_novo_contato(dicionario_contatos, "João Pedro", "21-56412435", "Joao.pedro@gmail.com")
adicionar_novo_contato(dicionario_contatos, "Kaio Jorge", "21-15171898", "Kaio.cruzeiro@gmail.com")
remover_contato(dicionario_contatos,3,"Kaio Jorge")
listar_contatos(dicionario_contatos)
```

> Explicação:

1. ``adicionar_novo_contato`` cria um novo id automaticamente usando max(dicionario.keys()) + 1 e adiciona o contato ao dicionário.
2. ``remover_contato`` solicita confirmação ao usuário antes de apagar o contato e usa pop(id) para remover.
3. ``listar_contatos`` percorre todos os contatos e imprime os detalhes formatados.
4. As funções permitem adicionar, remover e listar contatos de forma organizada.

**Próximo Capítulo : [Conjuntos set](../../aula_04/04_set.md)**
