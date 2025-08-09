from os import system
from time import sleep
from classes import Restaurante


def main():
    limpar_console()
    while True:
        titulo('Sabor Express')
        resposta_do_usuario = menu_de_opcoes('Selecione uma opção', 'Cadastrar restaurante', 'Listar restaurante', 'Ativar restaurante', 'Sair')
        if resposta_do_usuario == 1:
            cadastrar_restaurante()
        elif resposta_do_usuario == 2:
            listar_restaurantes()
        elif resposta_do_usuario == 3:
            ativar_restaurante()
        elif resposta_do_usuario == 4:
            finalizar_programa()
            break


def titulo(mensagem, linha='-', quantidade_de_espacos=50):
    print(linha * quantidade_de_espacos)
    print(mensagem.center(quantidade_de_espacos))
    print(linha * quantidade_de_espacos)


def input_continuar(msg=''):
    print(msg) if msg != '' else None
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
            input_continuar(f'Escolha inválida. Digite um número inteiro entre 1 e {len(opcoes)}.')
    elif not escolha.isdigit():
        input_continuar('Por favor, digite um número inteiro válido.')
    limpar_console()
    return


def pausa():
    sleep(1.5)


def limpar_console():
    system('cls')


def finalizar_programa():
    print('Saindo do programa...')
    pausa()
    limpar_console()
    print('Programa finalizado com sucesso.')
    exit(0)


def subtitulo(mensagem):
    limpar_console()
    titulo(mensagem)
        

def cadastrar_restaurante():
    msg_subtitulo = 'Cadastrar restaurante'
    restaurantes = Restaurante.listar_restaurantes()
    restaurante_nomes = [restaurante['nome'].upper() for restaurante in restaurantes] if restaurantes else []

    
    def pergunta_informacoes():
        while True:
            subtitulo(msg_subtitulo)
            listar_informacoes()
            pergunta = input('\nDeseja atualizar alguma informação [S/N]? ').strip().upper()
            if pergunta not in ('S', 'N'):
                input_continuar('Por favor, digite apenas S ou N.')
            else:
                return pergunta


    def atualizar_informacao():
        while True:
            subtitulo(msg_subtitulo)
            numero_informacao = menu_de_opcoes('Digite o número da informação a ser alterada', 'Nome')
            if numero_informacao == 1:
                nome_novo = cadastrar_nome_do_restaurante()
                input_continuar(f'Nome alterado de ({restaurante.nome}) para ({nome_novo}) com sucesso.')
                restaurante.nome = nome_novo
                break


    def listar_informacoes():
        for indice, (key, value) in enumerate(restaurante.get_dict_info().items(), start=1):
            print(f'{indice}. {key.title()}: {value} ')
  
                
    def cadastrar_nome_do_restaurante():
        while True:
            subtitulo(msg_subtitulo)
            nome = input('Digite o nome do restaurante que deseja cadastrar: ').strip()
            if not nome:
                input_continuar('Por favor, não deixe o espaço em branco.')
            else:
                if nome.upper() in restaurante_nomes:
                    input_continuar('Restaurante já cadastrado no sistema. Tente novamente.')
                else:
                    return nome
                
             
    restaurante = Restaurante(nome=cadastrar_nome_do_restaurante())
    while True:
        pergunta = pergunta_informacoes()
        if pergunta == 'S':
            atualizar_informacao()
        elif pergunta == 'N':
            subtitulo(msg_subtitulo)
            Restaurante.adicionar(restaurante)
            input_continuar(f'O cadastro do restaurante ({restaurante.nome}) foi concluido com sucesso!')
            main()


def listar_restaurantes():
    msg_subtitulo = 'Lista de restaurantes'
    subtitulo(msg_subtitulo)
    restaurantes = Restaurante.listar_restaurantes()
    if restaurantes:
        for indice, value in enumerate(restaurantes, start=1):
            print(f'{indice}. {value['nome']}')
        input_continuar()
    else:
        input_continuar('Ainda não há restaurantes cadastrados.')
    main()


def ativar_restaurante():
    pass
