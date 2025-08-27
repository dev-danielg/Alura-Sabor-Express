from os import system
from time import sleep
from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao


def main():
    limpar_console()
    titulo('Sabor Express')
    resposta_do_usuario = menu_de_opcoes('Selecione uma opção',
                                         ['Cadastrar restaurante',
                                          'Listar restaurante',
                                          'Ativar restaurante',
                                          'Avaliar restaurante',
                                          'Sair'],
                                         mostrar_opcoes=True,
                                         menu_principal=True)
    if resposta_do_usuario:
        if resposta_do_usuario == 1:
            cadastro_restaurante()
        elif resposta_do_usuario == 2:
            lista_de_restaurantes()
        elif resposta_do_usuario == 3:
            alternar_estado_restaurante()
        elif resposta_do_usuario == 4:
            cadastrar_avaliacao()
        elif resposta_do_usuario == 5:
            finalizar_programa()
    else:
        main()


def titulo(mensagem, linha='-', quantidade_de_espacos=100):
    print(linha * quantidade_de_espacos)
    print(mensagem.center(quantidade_de_espacos))
    print(linha * quantidade_de_espacos)


def enter_continuar(mensagem=''):
    print(mensagem) if mensagem != '' else None
    input('\nAperte "Enter" para continuar.\n')


def voltar_ao_menu():
    limpar_console()
    print('Voltando ao menu principal...')
    sleep(1.5)
    main()


def input_menu(mensagem):
    while True:
        resposta_do_usuario = input(
            f'{mensagem} (0 para voltar ao menu principal)\n'
            ).strip()
        if resposta_do_usuario == '0':
            voltar_ao_menu()
        else:
            return resposta_do_usuario


def menu_de_opcoes(mensagem, opcoes: list, mostrar_opcoes=True,
                   menu_principal=False):
    print(f'{mensagem} (0 para voltar ao menu principal)'
          if not menu_principal else mensagem)
    if mostrar_opcoes:
        for indice, opcao in enumerate(opcoes, start=1):
            print(f'[{indice}] {opcao}')
    escolha = input().strip()
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(opcoes):
            limpar_console()
            return escolha
        elif escolha == 0 and not menu_principal:
            voltar_ao_menu()
        else:
            if len(opcoes) == 1:
                frase_opcao = 'o número inteiro 1'
            else:
                frase_opcao = f'um número inteiro entre 1 e {len(opcoes)}'
            enter_continuar(f'Escolha inválida. Digite {frase_opcao}.')
    else:
        enter_continuar('Por favor, digite um número inteiro válido.')
    limpar_console()


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


def atualizar_informacao(tipo_info, info_antiga, funcao):
    info_nova = funcao()
    enter_continuar(
        (f'{tipo_info.title()} alterado de {info_antiga} para '
         f'{info_nova} com sucesso.')
        )
    return info_nova


def espaco_branco(resposta_do_usuario):
    if not resposta_do_usuario:
        enter_continuar('Por favor, não deixe o espaço em branco.')
        return True
    else:
        return False


def cadastro_restaurante():
    def atualizar_restaurante():
        while True:
            subtitulo(msg_subtitulo)
            resposta_do_usuario = menu_de_opcoes(
                'Digite o número da informação a ser alterada',
                ['Nome', 'Categoria']
            )
            if resposta_do_usuario:
                if resposta_do_usuario == 1:
                    info_nova = atualizar_informacao('nome',
                                                     restaurante.nome,
                                                     cadastro_nome)
                    restaurante.nome = info_nova
                elif resposta_do_usuario == 2:
                    info_nova = atualizar_informacao('categoria',
                                                     restaurante.categoria,
                                                     cadastro_categoria)
                    restaurante.categoria = info_nova
                return
            else:
                continue

    def adicionar_restaurante():
        subtitulo(msg_subtitulo)
        Restaurante.adicionar(restaurante)
        enter_continuar(
            (f'O cadastro do restaurante {restaurante.nome} '
             f'foi concluido com sucesso.')
        )

    def cadastro_nome():
        while True:
            subtitulo(msg_subtitulo)
            nome = input_menu(
                'Digite o nome do restaurante que deseja cadastrar'
            )
            if Restaurante.restaurante_existente(nome):
                enter_continuar('Restaurante já cadastrado no sistema.')
            else:
                return nome

    def cadastro_categoria():
        while True:
            subtitulo(msg_subtitulo)
            categoria = input_menu('Digite a categoria do restaurante')
            return categoria

    msg_subtitulo = 'Cadastrar restaurante'
    # restaurantes = Restaurante.retornar_lista()  # Removed as it is unused
    restaurante = Restaurante(nome=cadastro_nome(),
                              categoria=cadastro_categoria())
    while True:
        subtitulo(msg_subtitulo)
        restaurante.listar_informacoes()
        resposta_do_usuario = menu_de_opcoes(
            '\nDeseja atualizar alguma informação?', ['Sim', 'Não']
            )
        if resposta_do_usuario:
            if resposta_do_usuario == 1:
                atualizar_restaurante()
            elif resposta_do_usuario == 2:
                adicionar_restaurante()
                main()
        else:
            continue


def cadastrar_avaliacao():

    def cadastrar_nota():
        while True:
            subtitulo(msg_subtitulo)
            nota = input_menu('Digite uma nota de 1 a 5 para o restaurante')
            if nota.isdigit():
                nota = int(nota)
                if 1 <= nota <= 5:
                    return nota
                else:
                    enter_continuar(
                        'Por favor, digite um número inteiro entre 1 e 5.'
                    )
            else:
                enter_continuar(
                    'Por favor, digite um número inteiro válido'
                )

    def cadastrar_cliente():
        while True:
            subtitulo(msg_subtitulo)
            cliente = input_menu(
                'Digite o nome que deseja atribuir à sua avaliação'
                )
            return cliente

    def atualizar_avaliacao():
        while True:
            subtitulo(msg_subtitulo)
            resposta_do_usuario = menu_de_opcoes(
                                  'Deseja atualizar qual informação?',
                                  ['Seu nome',
                                   'Nota'])
            if resposta_do_usuario:
                if resposta_do_usuario == 1:
                    info_nova = atualizar_informacao('nome',
                                                     avaliacao.cliente,
                                                     cadastrar_cliente)
                    avaliacao.cliente = info_nova
                elif resposta_do_usuario == 2:
                    info_nova = atualizar_informacao('nota',
                                                     avaliacao.nota,
                                                     cadastrar_nota)
                    avaliacao.nota = info_nova
                return
            else:
                continue

    def adicionar_avaliacao():
        subtitulo(msg_subtitulo)
        restaurante.receber_avaliacao(avaliacao)
        enter_continuar(
            (f'Avaliação de {avaliacao.nota} estrelas '
             f'aplicada ao restaurante {restaurante.nome} com sucesso.')
            )

    msg_subtitulo = 'Avaliar restaurante'
    restaurantes = Restaurante.retornar_lista()
    while True:
        subtitulo(msg_subtitulo)
        Restaurante.listar_restaurantes()
        if restaurantes:
            resposta_do_usuario = menu_de_opcoes(
                                  '\nDigite o número do restaurante que '
                                  'deseja avaliar',
                                  restaurantes,
                                  mostrar_opcoes=False)
            if resposta_do_usuario:
                restaurante = restaurantes[resposta_do_usuario - 1]
                avaliacao = Avaliacao(cliente=cadastrar_cliente(),
                                      nota=cadastrar_nota())
                subtitulo(msg_subtitulo)
                avaliacao.listar_informacoes()
                resposta_do_usuario = menu_de_opcoes(
                    '\nDeseja atualizar alguma informação?', ['Sim', 'Não'])
                if resposta_do_usuario == 1:
                    atualizar_avaliacao()
                elif resposta_do_usuario == 2:
                    adicionar_avaliacao()
                    main()
            else:
                continue
        else:
            enter_continuar()
            main()


def lista_de_restaurantes():
    msg_subtitulo = 'Lista de restaurantes'
    subtitulo(msg_subtitulo)
    Restaurante.listar_restaurantes()
    enter_continuar()
    main()


def alternar_estado_restaurante():
    msg_subtitulo = 'Ativar/Desativar restaurantes'
    restaurantes = Restaurante.retornar_lista()
    while True:
        subtitulo(msg_subtitulo)
        Restaurante.listar_restaurantes()
        if restaurantes:
            resposta_do_usuario = menu_de_opcoes(
                                  '\nDigite o número do restaurante '
                                  'que deseja ativar ou desativar',
                                  restaurantes,
                                  False)
            if resposta_do_usuario:
                restaurante = restaurantes[resposta_do_usuario - 1]
                restaurante.atualizar_estado()
                enter_continuar(
                    f'Restaurante {restaurante.nome} '
                    f'{restaurante.estado.lower()} com sucesso.'
                )
                main()
            else:
                continue
        else:
            enter_continuar()
            main()
