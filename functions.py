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
            lista_de_restaurantes()
        elif resposta_do_usuario == 3:
            alternar_estado_restaurante()
        elif resposta_do_usuario == 4:
            finalizar_programa()


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
    else:
        input_continuar('Por favor, digite um número inteiro válido.')
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
            listar_informacoes()
            pergunta = input('\nDeseja atualizar alguma informação [S/N]? ').strip().upper()
            if pergunta not in ('S', 'N'):
                input_continuar('Por favor, digite apenas S ou N.')
            else:
                return pergunta


    def atualizar_informacao():

        
        def atualizar_nome():
            nome_novo = cadastrar_nome_do_restaurante()
            input_continuar(f'Nome alterado de ({restaurante.nome}) para ({nome_novo}) com sucesso.')
            restaurante.nome = nome_novo


        def atualizar_categoria():
            categoria_nova = cadastrar_categoria()
            input_continuar(f'Categoria alterada de ({restaurante.categoria}) para ({categoria_nova}) com sucesso.')
            restaurante.categoria = categoria_nova


        while True:
            subtitulo(msg_subtitulo)
            numero_informacao = menu_de_opcoes('Digite o número da informação a ser alterada', 'Nome', 'Categoria')
            if numero_informacao == 1:
                atualizar_nome()
            elif numero_informacao == 2:
                atualizar_categoria()
    
    
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
                if restaurantes:
                    for restaurante in restaurantes:
                        if nome.upper() == restaurante['nome'].upper():
                            input_continuar('Restaurante já cadastrado no sistema. Tente novamente.')
                            break
                        elif restaurante == restaurantes[-1]:
                            return nome
                else:
                    return nome
                        
                
    def cadastrar_categoria():
        while True:
            subtitulo(msg_subtitulo)
            categoria = input('Digite a categoria do restaurante: ').strip()
            if not categoria:
                input_continuar('Por favor, não deixe o espaço em branco.')
            else:
                return categoria
    
    
    msg_subtitulo = 'Cadastrar restaurante'
    restaurantes = Restaurante.retornar_lista()
    restaurante = Restaurante(nome=cadastrar_nome_do_restaurante(), 
                              categoria=cadastrar_categoria(), 
                              estado='Desativado')
    while True:
        pergunta = pergunta_informacoes()
        if pergunta == 'S':
            atualizar_informacao()
        elif pergunta == 'N':
            subtitulo(msg_subtitulo)
            Restaurante.adicionar(restaurante)
            input_continuar(f'O cadastro do restaurante ({restaurante.nome}) foi concluido com sucesso.')
            main()
            

def lista_de_restaurantes():
    msg_subtitulo = 'Lista de restaurantes'
    subtitulo(msg_subtitulo)
    Restaurante.listar_restaurantes()
    input_continuar()
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
                    restaurante_escolhido = restaurantes[escolha - 1]
                    restaurante = Restaurante(nome=restaurante_escolhido['nome'], 
                                            categoria=restaurante_escolhido['categoria'], 
                                            estado=restaurante_escolhido['estado'])
                    restaurante.mudar_estado()
                    Restaurante.atualizar_estado(escolha, restaurante.estado)
                    input_continuar(f'Restaurante ({restaurante.nome}) {restaurante.estado.lower()} com sucesso.')
                    main()
                else:
                    input_continuar(f'Por favor, digite um número inteiro entre 1 e {len(restaurantes)}')
            else:
                input_continuar('Por favor, digite um número inteiro válido.')
        else:
            input_continuar()
            main()
