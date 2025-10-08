# 📝 Exercícios Resolvidos — Aula 13 (Módulo 2)

Nesta aula, trabalhamos a criação e chamada de funções simples.
O objetivo é compreender como funções ajudam na organização e reutilização do código.

---

## [🔹 1. Função de Apresentação](Ex_01.py)

```python
def apresentacao(nome, curso):
    return f"Olá, meu nome é {nome} e sou do curso de {curso}"

aluno1 = apresentacao("Pedro Henrique", "Psicologia")
print(aluno1)
```

> 📌 Explicação: A função recebe nome e curso como parâmetros e retorna uma frase personalizada.

---

## [🔹 2. Funções de Menu com Dicionário](Ex_02.py)

```python
def inicio():
    print("Função inicio inicializada.")

def ajuda():
    print("Função ajuda inicializada.")

def sair():
    print("Função sair inicializada.")

def menu(num_opcao):
    lista_opcoes = {1: inicio, 2: ajuda, 3: sair}
    
    if num_opcao in lista_opcoes:
        lista_opcoes[num_opcao]()
    else:
        print("Essa opção não existe no menu.")

menu(0)
menu(1)
menu(2)
menu(3)
```

> 📌 Explicação: Usamos um dicionário de funções para mapear opções do menu. Se a opção existir, chamamos a função correspondente. Caso contrário, exibimos uma mensagem de erro.

---

## [🔹 3. Função Separadora](Ex_03.py)

```python
def separador():
    print("=" * 40)

print("Iniciando programa ...")
separador()
print("Processando ...")
separador()
print("Fim do programa ...")
```

> 📌 Explicação: A função ``separador()`` imprime uma linha de =, ajudando a organizar a saída do programa.

**Próximo Capítulo : [Declaração de Funções](../../aula_14/14_declaracao_de_funcoes.md)**
