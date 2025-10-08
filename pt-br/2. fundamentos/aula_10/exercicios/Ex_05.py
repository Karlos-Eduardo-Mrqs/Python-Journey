# Use enumerate() para imprimir as tarefas com numeração a partir de 1:

tarefas = ["Lavar a louça", "Estudar Python", "Fazer exercícios", "Ler um livro"]

for indice, tarefa in enumerate(tarefas):
    print(f"{indice + 1} : {tarefa}")