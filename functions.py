from os import system
from time import sleep
from modelos.restaurante import Restaurante


def main():
    limpar_console()
    titulo('Sabor Express')
    resposta_do_usuario = menu_de_opcoes('Selecione uma opção', 'Cadastrar restaurante', 'Listar restaurante', 'Ativar restaurante', 'Sair')
    if resposta_do_usuario == 1:
        cadastrar_restaurante()
    elif resposta_do_usuario == 2:
        lista_de_restaurantes()
    elif resposta_do_usuario == 3:
        alternar_estado_restaurante()
    elif resposta_do_usuario == 4:
        finalizar_programa()
    else:
        main()


def titulo(mensagem, linha='-', quantidade_de_espacos=50):
    print(linha * quantidade_de_espacos)
    print(mensagem.center(quantidade_de_espacos))
    print(linha * quantidade_de_espacos)


def continuar(mensagem=''):
    print(mensagem) if mensagem != '' else None
    input('\nAperte "Enter" para continuar.\n')


def menu_de_opcoes(mensagem, *opcoes):
    print(mensagem)
    for indice, opcao in enumerate(opcoes, start=1):
        print(f'[{indice}] {opcao}')
    escolha = input().strip()
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(opcoes):
            limpar_console()
            return escolha
        else:
            continuar(f'Escolha inválida. Digite um número inteiro entre 1 e {len(opcoes)}.')
    else:
        continuar('Por favor, digite um número inteiro válido.')
    limpar_console()
    return


def limpar_console():
    system('cls')


def finalizar_programa():
    print('Saindo do programa...')
    sleep(1.5)
    limpar_console()
    print('Programa finalizado com sucesso.')
    exit(0)


def subtitulo(mensagem):
    limpar_console()
    titulo(mensagem)
        

def cadastrar_restaurante():

    
    def pergunta_informacoes():
        while True:
            subtitulo(msg_subtitulo)
            restaurante.listar_informacoes()
            pergunta = input('\nDeseja atualizar alguma informação [S/N]? ').strip().upper()
            if pergunta not in ('S', 'N'):
                continuar('Por favor, digite apenas S ou N.')
            else:
                return pergunta


    def atualizar_informacao():

        
        def atualizar_nome():
            nome_novo = cadastrar_nome_do_restaurante()
            continuar(f'Nome alterado de ({restaurante.nome}) para ({nome_novo}) com sucesso.')
            restaurante.nome = nome_novo


        def atualizar_categoria():
            categoria_nova = cadastrar_categoria()
            continuar(f'Categoria alterada de ({restaurante.categoria}) para ({categoria_nova}) com sucesso.')
            restaurante.categoria = categoria_nova


        while True:
            subtitulo(msg_subtitulo)
            numero_informacao = menu_de_opcoes('Digite o número da informação a ser alterada', 'Nome', 'Categoria')
            if numero_informacao:
                if numero_informacao == 1:
                    atualizar_nome()
                elif numero_informacao == 2:
                    atualizar_categoria()
                break
  

    def cadastrar_nome_do_restaurante():
        while True:
            subtitulo(msg_subtitulo)
            nome = input('Digite o nome do restaurante que deseja cadastrar: ').strip()
            if not nome:
                continuar('Por favor, não deixe o espaço em branco.')
            else:
                if Restaurante.restaurante_existente(nome):
                    continuar('Restaurante já cadastrado no sistema.')
                else:
                    return nome
                        
                
    def cadastrar_categoria():
        while True:
            subtitulo(msg_subtitulo)
            categoria = input('Digite a categoria do restaurante: ').strip()
            if not categoria:
                continuar('Por favor, não deixe o espaço em branco.')
            else:
                return categoria
    
    
    msg_subtitulo = 'Cadastrar restaurante'
    restaurantes = Restaurante.retornar_lista()
    restaurante = Restaurante(nome=cadastrar_nome_do_restaurante(), 
                              categoria=cadastrar_categoria())
    while True:
        pergunta = pergunta_informacoes()
        if pergunta == 'S':
            atualizar_informacao()
        elif pergunta == 'N':
            subtitulo(msg_subtitulo)
            Restaurante.adicionar(restaurante)
            continuar(f'O cadastro do restaurante ({restaurante.nome}) foi concluido com sucesso.')
            main()
            

def lista_de_restaurantes():
    msg_subtitulo = 'Lista de restaurantes'
    subtitulo(msg_subtitulo)
    Restaurante.listar_restaurantes()
    continuar()
    main()


def alternar_estado_restaurante():
    msg_subtitulo = 'Ativar/Desativar restaurantes'
    while True:
        subtitulo(msg_subtitulo)
        restaurantes = Restaurante.retornar_lista()
        Restaurante.listar_restaurantes()
        if restaurantes:
            escolha = input('\nDeseja ativar ou desativar qual restaurante?\n').strip()
            if escolha.isdigit():
                escolha = int(escolha)
                if 1 <= escolha <= len(restaurantes):
                    restaurante = restaurantes[escolha - 1]
                    restaurante.atualizar_estado()
                    continuar(f'Restaurante ({restaurante.nome}) {restaurante.estado.lower()} com sucesso.')
                    main()
                else:
                    continuar(f'Por favor, digite um número inteiro entre 1 e {len(restaurantes)}')
            else:
                continuar('Por favor, digite um número inteiro válido.')
        else:
            continuar()
            main()
