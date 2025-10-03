print('oi')
banco_de_dados=[]

def adicionar_tarefa():
    #adiciona uma nova tarefa ao banco de dados
    tarefa1= {
        'nome':input('Digite o nome da tarefa: ') , 
        'descricao': input('Digite a descrição da tarefa: '), 
        'prioridade':int(input('Digite a prioridade da tarefa(1-5): ')), 
        'categoria':input('Digite a categoria da tarefa: '), 
        'concluido': False,}
    banco_de_dados.append(tarefa1)
    print('\nTarefa adicionada com sucesso!\n')

def listar_tarefas():
    print(banco_de_dados)

while True:
    print('='*50)
    print('Gerenciador de tarefas')
    print('='*50)
    print('Selecione uma opção')
    print('1 -Adicionar Tarefa')
    print('2 - Listar Todas as Tarefas')
    print('3 - Sair')
    op=int(input('->'))
    if op ==1:
        adicionar_tarefa()
    elif op==2:
        listar_tarefas()
    elif op==3: 
        break
    else:
        print('\nOPÇÃO INVÁLIDA\n')















# tarefa2= {
    # 'nome':input('Digite o nome da tarefa: ') , 
    # 'descricao': input('Digite a descrição da tarefa: '), 
    # 'prioridade':int(input('Digite a prioridade da tarefa(1-5): ')), 
    # 'categoria':input('Digite a categoria da tarefa: '), 
    # 'concluido': False,}

# tarefa3= {
#     'nome':input('Digite o nome da tarefa: ') , 
#     'descricao': input('Digite a descrição da tarefa: '), 
#     'prioridade':int(input('Digite a prioridade da tarefa(1-5): ')), 
#     'categoria':input('Digite a categoria da tarefa: '), 
#     'concluido': False,}

# tarefa4= {
#     'nome':input('Digite o nome da tarefa: ') , 
#     'descricao': input('Digite a descrição da tarefa: '), 
#     'prioridade':int(input('Digite a prioridade da tarefa(1-5): ')), 
#     'categoria':input('Digite a categoria da tarefa: '), 
#     'concluido': False,}






