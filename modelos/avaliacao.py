class Avaliacao:
    _cliente: str
    _nota: float
    
    
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
    
    
    def to_dict(self):
        return {'cliente': self.cliente, 
                'nota': self.nota}
    
    
    @property
    def cliente(self):
        return self._cliente
    
    
    @property
    def nota(self):
        return self._nota
    
    
    @cliente.setter
    def cliente(self, novo_cliente):
        self._cliente = novo_cliente
        
    
    @nota.setter
    def nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
        