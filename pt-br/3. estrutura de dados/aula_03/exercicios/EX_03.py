def adicionar_novo_contato(dicionario: dict,nome:str,telefone:str,email:str):
    if dicionario: 
        id_contato = max(dicionario_contatos.keys()) + 1
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
    1: {"nome":str("Lucas Moura"), "telefone":str("21-07889223"), "email":str("LucasMoura@gmail.com")}
}

adicionar_novo_contato(dicionario_contatos, "João Pedro", "21-56412435", "Joao.pedro@gmail.com")
adicionar_novo_contato(dicionario_contatos, "Kaio Jorge", "21-15171898", "Kaio.cruzeiro@gmail.com")
remover_contato(dicionario_contatos,3,"Kaio Jorge")
listar_contatos(dicionario_contatos)
