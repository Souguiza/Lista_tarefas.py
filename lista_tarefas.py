tarefas = []

def mostrar_menu():
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append({"tarefa": tarefa, "concluida": False})
        print("Tarefa adicionada!")

    elif escolha == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas:")
            for i, t in enumerate(tarefas):
                status = "✓" if t["concluida"] else "✗"
                print(f"{i+1}. {t['tarefa']} [{status}]")

    elif escolha == "3":
        if not tarefas:
            print("Nenhuma tarefa para marcar como concluída.")
        else:
            for i, t in enumerate(tarefas):
                status = "✓" if t["concluida"] else "✗"
                print(f"{i+1}. {t['tarefa']} [{status}]")
            indice = int(input("Digite o número da tarefa concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["concluida"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número inválido.")
    elif escolha == "4":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            for i, t in enumerate(tarefas):
                status = "✓" if t["concluida"] else "✗"
                print(f"{i+1}. {t['tarefa']} [{status}]")
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida['tarefa']}' removida!")
            else:
                print("Número inválido.")
    elif escolha == "5":
        print("Saindo do programa... Até logo!")
        break

