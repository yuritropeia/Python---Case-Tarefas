import json

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)
    print("Tarefas salvas com sucesso!")

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
            print("Tarefas carregadas com sucesso!")
            return tarefas
    except:
        print("Nenhum arquivo de tarefas encontrado! Começando uma nova lista.")
        return []


def adicionar_tarefa(nome, prioridade):
    tarefa = {
            'nome': nome,
            'prioridade': prioridade
        }

    tarefas.append(tarefa)
    print("Tarefa adicionada: ", tarefa)

def listar_tarefas():
    print ('Lista de Tarefas: ')
    for tarefa in tarefas:
            print(f"- {tarefa['nome']} (Prioridade {tarefa['prioridade']})")

def remover_tarefa(nome):
    for tarefa in tarefas:
            if tarefa['nome'] == nome:
                tarefas.remove(tarefa)
                print("Tarefa removida: ", nome)
                break
            else:
                print("Tarefa não encontrada!")

tarefas = carregar_tarefas()

while True:
    print("** Menu de Opções **")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Salvar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        nome = input("Digite uma tarefa: ")
        prioridade = input("Digite a prioridade da tarefa: ")

        adicionar_tarefa(nome, prioridade)    
        

    elif opcao == '2':
        listar_tarefas()
    
    elif opcao == '3':
        nome = input("Digite a tarefa a ser removida: ")
        remover_tarefa(nome)
    
    elif opcao == '4':
        salvar_tarefas()

    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

