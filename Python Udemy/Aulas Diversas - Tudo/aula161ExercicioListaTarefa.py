# EXercicio - Lista de Tarefa com desfazer e refazer 

def listar(tarefas):
    print()
    if not tarefas:
        print()
        print("Nenhuma tarefa para listar")
        return
    

    print("Tarefas: ")
    for tarefa in tarefas:
        print(f"\t{tarefa}")


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print("Nenhuma tarefa para desfazer")
        return
    


    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print()



def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print("Você não digitou uma tarefa ")
        return
    tarefas.append(tarefa)
    


    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print("Nenhuma tarefa para refazer")
        return
    


    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)



tarefas = []
tarefas_refazer = []


while True: 
    print("Comandos: listar, desfazer e refazer")
    tarefa = input("Digite uma tarefa ou comando: \n")
    
    if tarefa == "listar":
        listar(tarefas)
        continue
    elif tarefa == "desfazer":
        desfazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == "refazer":
        refazer(tarefas, tarefas_refazer)
        continue
    else: 
        adicionar(tarefa, tarefas)
        continue