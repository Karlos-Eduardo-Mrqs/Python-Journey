def verificar_idade(idade):
    classifica_idade = {
        "Menor de idade !": idade < 18, 
        "Maior de idade !": idade >= 18
        }
    for mensagem,valor_verdadeiro in classifica_idade.items():
        if valor_verdadeiro:
            print(f"Se você tem {idade} anos, então você é {mensagem}")

verificar_idade(20)
verificar_idade(18)
verificar_idade(30)
verificar_idade(14)
