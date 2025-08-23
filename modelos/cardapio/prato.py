from item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    _descricao: str
    
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def to_dict(self):
        dicionario = super().to_dict()
        dicionario['descricao'] = self.descricao
        return dicionario
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        