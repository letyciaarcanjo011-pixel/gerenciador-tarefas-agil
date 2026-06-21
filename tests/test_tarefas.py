from src.tarefas import *

def test_criar_tarefa():
    tarefas.clear()
    criar_tarefa("Estudar")
    assert len(tarefas) == 1