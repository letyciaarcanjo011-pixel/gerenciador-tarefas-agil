from tarefas import *

while True:
    print("\n1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ")
        criar_tarefa(nome)

    elif opcao == "2":
        print(listar_tarefas())

    elif opcao == "3":
        indice = int(input("Número: "))
        novo = input("Novo nome: ")
        editar_tarefa(indice, novo)

    elif opcao == "4":
        indice = int(input("Número: "))
        excluir_tarefa(indice)

    elif opcao == "5":
        breaks