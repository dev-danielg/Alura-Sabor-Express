from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    _nome: str
    _categoria: str
    _estado: bool
    _avaliacoes: list
    _cardapio: list
    _restaurantes_cadastrados: list = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._estado = False
        self._avaliacoes = []
        self._cardapio = []

    def to_dict(self):
        return {'nome': self.nome,
                'categoria': self.categoria,
                'estado': self.estado,
                'avaliacao': self.avaliacao}

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def estado(self):
        return 'Ativado' if self._estado else 'Desativado'

    @property
    def avaliacoes(self):
        if self._avaliacoes:
            return self._avaliacoes

    @property
    def avaliacao(self):
        if self.avaliacoes:
            soma = sum(avaliacao.nota for avaliacao in self.avaliacoes)
            media = round(soma / len(self.avaliacoes), 1)
            return media
        else:
            return '-'

    @property
    def cardapio(self):
        if self._cardapio:
            for indice, item in enumerate(self._cardapio, start=1):
                mensagem = "Informações do item indisponíveis."
                if hasattr(item, 'descricao'):
                    mensagem = f'{indice}. Nome: {item.nome} | '
                    f'Preço: {item.preco} | '
                    f'Descrição: {item.descricao}'
                elif hasattr(item, 'tamanho'):
                    mensagem = f'{indice}. Nome: {item.nome} | '
                    f'Preço: {item.preco} | '
                    f'Tamanho: {item.tamanho}'
                print(mensagem)
        else:
            return '-'

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria.title()

    def atualizar_estado(self):
        self._estado = not self._estado

    def listar_informacoes(self):
        print(f'''Nome: {self.nome}
Categoria: {self.categoria}''')

    def receber_avaliacao(self, avaliacao):
        self._avaliacoes.append(avaliacao)

    def adicionar_no_cardapio(self, item):
        if isinstance(self, ItemCardapio):
            self._cardapio.append(item)

    @classmethod
    def listar_restaurantes(cls, espaco=100, ajuste=25):
        restaurantes = cls.retornar_lista()
        if restaurantes:
            print(
                  f'{'NOME'.ljust(25)} | '
                  f'{'CATEGORIA'.ljust(ajuste)} | '
                  f'{'AVALIAÇÃO'.ljust(ajuste)} | '
                  'ESTADO'
            )
            print('-' * espaco)
            for indice, restaurante in enumerate(restaurantes, start=1):
                print(
                      f'{f'{indice}. {restaurante.nome}'.ljust(25)} | '
                      f'{restaurante.categoria.ljust(ajuste)} | '
                      f'{str(restaurante.avaliacao).ljust(ajuste)} |'
                      f'{restaurante.estado}'
                )
        else:
            print('Não há restaurantes cadastrados no sistema.')

    @classmethod
    def retornar_lista(cls):
        return cls._restaurantes_cadastrados

    @classmethod
    def restaurante_existente(cls, nome):
        if cls._restaurantes_cadastrados:
            return any(
                restaurante.nome.upper() == nome.upper()
                for restaurante in cls._restaurantes_cadastrados
            )
        else:
            return False

    @classmethod
    def adicionar(cls, restaurante):
        cls._restaurantes_cadastrados.append(restaurante)
