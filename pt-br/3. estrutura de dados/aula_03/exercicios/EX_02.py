def media_turma(dicionario:dict) -> float:
    notas = [aluno['nota'] for aluno in dicionario.values()]
    return sum(notas) / len(notas)

def listar_alunos_media_alta(dicionario:dict,media:float):
    print("Alunos acima da média:")
    for id,aluno in dicionario.items():
        if aluno["nota"] > media:
            print(f"Id: {id} | Nome : {aluno['nome']}")
    
print("------------------------------------")

dicionario_alunos = {
    1: {"nome":"Pedro Fonseca","nota":float(9.5)},
    2: {"nome":"Yan Sacramento","nota":float(10.0)},
    3: {"nome":"João Macedo","nota":float(8.5)},
    4: {"nome":"Miguel Santos","nota":float(7.5)},
    5: {"nome":"Caua Souza","nota":float(8.5)}, 
    6: {"nome":"Victor Goldman","nota":float(10.0)}, 
}

media = media_turma(dicionario_alunos)
print(f"A média da turma é {media:.1f}")
print("------------------------------------")

dicionario_alunos[5]["nota"] = 9.4
listar_alunos_media_alta(dicionario_alunos,media)
