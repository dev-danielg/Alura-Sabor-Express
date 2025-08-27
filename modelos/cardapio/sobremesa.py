from item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    _tipo: str
    _tamanho: str
    _descricao: str

    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def to_dict(self):
        dicionario = super().to_dict()
        dicionario["tipo"] = self.tipo
        dicionario["tamanho"] = self.tamanho
        dicionario["descricao"] = self.descricao
        return dicionario

    @property
    def tipo(self):
        return self._tipo

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def descricao(self):
        return self._descricao

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    def aplicar_desconto(self):
        self._preco = self._preco * 0.9
