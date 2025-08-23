class ItemCardapio:
    _nome: str
    _preco: float
    
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    def to_dict(self):
        return {'nome': self.nome, 'preco': self.preco}
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return f'R$ {self._preco:.2f}'.replace('.', ',')
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @preco.setter
    def preco(self, preco):
        self._preco = preco
    