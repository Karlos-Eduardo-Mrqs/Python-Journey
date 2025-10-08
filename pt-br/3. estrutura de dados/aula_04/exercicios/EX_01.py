def listar_turma(set_lista:set,status:str):
    print(status)
    
    print("--------------------------------------------------")
    for aluno in set_lista:
        print(aluno)
    print("--------------------------------------------------")

turma_manha = {"Carlos", "Ana", "Beatriz"}
todos_manha = {"Carlos", "Ana", "Beatriz", "Pedro", "Lucas"}

lista_alunos_em_todas_as_turmas = turma_manha.intersection(todos_manha)
lista_alunos_somente_na_manha = todos_manha.difference(turma_manha)
qtd_alunos = len(turma_manha.union(todos_manha))

print(f"Temos no total {qtd_alunos} alunos em todas as turmas !")

listar_turma(lista_alunos_em_todas_as_turmas,"Alunos que estão em todas as turmas")
listar_turma(lista_alunos_somente_na_manha,"Alunos que estão somente de manhã")
