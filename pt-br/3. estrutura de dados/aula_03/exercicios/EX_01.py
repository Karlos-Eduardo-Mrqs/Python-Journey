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
    4: {"nome":"?????","idade":00,"salario":1200.00},
}

listar_funcionarios(dicionarios_funcionarios,"Lista original sem alterações")

dicionarios_funcionarios[3]['salario'] = 1562.70
dicionarios_funcionarios.pop(4)

listar_funcionarios(dicionarios_funcionarios,"Lista atualizada")