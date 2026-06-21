tarefas = []

def criar_tarefa(nome):
    tarefas.append(nome)

def listar_tarefas():
    return tarefas

def editar_tarefa(indice, novo_nome):
    tarefas[indice] = novo_nome

def excluir_tarefa(indice):
    tarefas.pop(indice)