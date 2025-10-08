def remover_repeticao(lista:list) -> set:
    lista_nova = set()
    for numero in lista:
        lista_nova.add(numero)
    return lista_nova

def listar_set(set_lista:set,status:str):    
    print(status)
    print("-----------------------------------------------------")
    for numero in set_lista: 
        print(f"Numero : {numero}")
    print("-----------------------------------------------------")

lista_numeros = [1, 2, 3, 2, 4, 3, 5, 1, 6] 
lista_nova = remover_repeticao(lista_numeros)
listar_set(lista_nova,"Lista nova sem repetição ! ")

lista_nova.add(7)
lista_nova.remove(3)

listar_set(lista_nova,"Lista atualizada !")
