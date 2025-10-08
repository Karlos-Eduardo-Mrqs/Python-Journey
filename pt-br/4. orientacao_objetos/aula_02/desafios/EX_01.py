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