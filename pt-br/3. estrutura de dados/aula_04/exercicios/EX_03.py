def listar_aprovados(lista_aprovados:set,status:str):
    print(status)
    print("--------------------------------------------------")
    for aprovado in lista_aprovados:
        print(aprovado)
    print("--------------------------------------------------")

aprovados_matematica = {"Eduardo", "Ana", "Beatriz", "Lucas", "Pedro", "Mariana", "Juliana"}
aprovados_portugues = {"Ana", "Beatriz", "Pedro", "Lucas", "Marcos", "Juliana", "Fernanda"}

lista_aprovados_em_ambas = aprovados_matematica.intersection(aprovados_portugues)
lista_aprovados_em_portugues = aprovados_portugues.difference(aprovados_matematica)
lista_aprovados_em_matematica = aprovados_matematica.difference(aprovados_portugues)

listar_aprovados(lista_aprovados_em_ambas,"Aprovados em todas as matérias")
listar_aprovados(lista_aprovados_em_portugues,"Aprovados em Português")
listar_aprovados(lista_aprovados_em_matematica,"Aprovados em Matemática")