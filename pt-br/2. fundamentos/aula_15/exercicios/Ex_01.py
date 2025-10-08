def estatisticas(lista_num):
    media_lista_num = (sum(lista_num) / len(lista_num))
    print(f"Maior Numero : {max(lista_num)} | Menor Numero : {min(lista_num)} | Media : {media_lista_num:.2f}")
    

estatisticas([5,6,7,8,12,9,15,8,13,4,2,1])