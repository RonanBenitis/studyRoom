import os

# Definindo em escopo global
# Lista de dicionarios
restaurantes = [
                {'nome':'a', 'categoria':'1', 'ativo':False},
                {'nome':'b', 'categoria':'2', 'ativo':True},
                {'nome':'c', 'categoria':'3', 'ativo':False},
                ]

def exibir_nome_do_programa():
    '''Exibir o logo do cliente no prompt ao iniciar o programa '''
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def finalizar_app():
    '''Chama a função exibir_subtitulo com o texto 'Finalizando o app'
    encerrando a aplicação em seguida, por não chamar a
    função main novamente
    '''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Pede uma tecla pra voltar ao menu principal
    
    Outpus:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_opcoes():
    '''Exibir as opção abaixo listadas no prompt
    Essa função apenas exibi, não possui inputs
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Limpa o console e exibe um subtítulo estilizado na tela
    
    Inputs:
    - texto: (str) O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print() # Outra forma de pular linha

def cadastrar_novo_reastaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    # Não realizamos o casting pois queremos que seja string mesmo
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} 
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_resturante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_resturante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante. 
    O usuário insere o nome do restaurante, voltando ao menu no final
    da execução da função.

    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    ou
    - Exibe mensagem indicando que não achou o restaurante
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            # Palavra reservada not (inversão)
            restaurante['ativo'] = not restaurante['ativo']
            # Utilizando ternário
            print(f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi destivado com sucesso')
            voltar_ao_menu_principal()
            break

    print(f'O restaurante {nome_restaurante} não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário, sendo cada opção
    uma função condizente com a opção escolhida.
    - O titulo das opções é demonstrada por outra função
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_reastaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()