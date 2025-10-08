def inicio():
    print("Função inicio inicializada.")

def ajuda():
    print("Função ajuda inicializada.")

def sair():
    print("Função sair inicializada.")

def menu(num_opcao):
    lista_opcoes = {1:inicio, 2:ajuda, 3:sair}
    
    if num_opcao in lista_opcoes:
        lista_opcoes[num_opcao]()
    else:
        print("Essa opção não existe no menu.")

menu(0)
menu(1)
menu(2)
menu(3)