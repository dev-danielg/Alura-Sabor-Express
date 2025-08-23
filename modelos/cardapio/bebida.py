from item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    _nome: str
    _preco: float
    _tamanho: str
    
    def __init__(self, nome, preco, tamanho):
        self._nome = nome
        self._preco = preco
        self._tamanho = tamanho
    
    def to_dict(self):
        dicionario = super().to_dict()
        dicionario['tamanho'] = self.tamanho
        return dicionario
    
    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho