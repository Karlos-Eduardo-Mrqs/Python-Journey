# Exercício de Encapsulamento em Python — Aula 02 (Módulo 4)

Este exercício aborda orientação a objetos com foco em atributos privados, métodos de acesso e alteração segura de dados.

---

## [🔹 Classe Aluno com notas](EX_01.py)

```py
class Aluno:
    def __init__(self,nome:str,notas:list):
        self.__nome = nome
        self.__notas = notas
    
    def alterar_notas(self):
        print(f"Alterando Nota de {self.__nome}")
        for indice , nota in enumerate(self.__notas):
            print(f" [{indice + 1}] = {nota} ") 

        indice_alterado = int(input("Qual é a nota que você deseja alterar ?:"))
        
        if 1 <= indice_alterado <= len(self.__notas): 
            nova_nota = float(input("Digite a nova nota:"))
            if nova_nota > 0: 
                print("✅ Nota alterada com sucesso!")
                self.__notas[indice_alterado - 1] = nova_nota
            else:
                print("⚠️ A nota não pode ser negativa.")
        else:
            print("⚠️ Índice inválido.")

    def consultar_notas(self):
        print(f"Consultando Notas de {self.__nome}")
        for indice , nota in enumerate(self.__notas,start=1):
            print(f" [{indice}] = {nota} ") 
            
aluno = Aluno("Gabriel Moraes",[0,10,9.5,7.5,6.5])
aluno.consultar_notas()
aluno.alterar_notas()
aluno.consultar_notas()
```

> Explicação

- Atributos privados (``__nome`` e ``__notas``)

1. O duplo underline (__) antes do nome do atributo indica que ele não deve ser acessado diretamente fora da classe.
2. Isso protege os dados internos do objeto e força o uso de métodos para manipulação.

- Método ``consultar_notas()``

1. Percorre a lista de notas usando enumerate para mostrar o índice e o valor de cada nota.
2. Permite ao usuário visualizar as notas de forma organizada.

- Método ``alterar_notas()``

1. Mostra todas as notas e pede ao usuário qual deseja alterar.
2. Verifica se o índice fornecido é válido ``(1 <= índice <= tamanho da lista)``.
3. Solicita a nova nota e garante que ela não seja negativa.
4. Atualiza a nota correspondente na lista de forma segura.

- Fluxo do programa

1. Primeiro, o método ``consultar_notas()`` mostra as notas originais.
2. Em seguida, ``alterar_notas()`` permite que o usuário altere uma nota específica.
3. Por fim, ``consultar_notas()`` exibe a lista atualizada, mostrando a alteração realizada.

---

## ✅ Conceitos abordados

1. *Encapsulamento:* uso de atributos privados para proteger os dados do objeto.
2. *Métodos de acesso e modificação:* ``consultar_notas()`` e ``alterar_notas()`` controlam como as notas são lidas e alteradas.
3. *Validação de dados:* verifica índices válidos e impede que notas negativas sejam atribuídas.
4. *Interatividade com o usuário:* usa ``input()`` para receber comandos e valores.

**Próximo Capítulo : [Herança](../../aula_03/03_heranca.md)**
