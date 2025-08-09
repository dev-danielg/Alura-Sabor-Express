class Restaurante:
    nome: str
    estado: str
    restaurantes_cadastrados = []
    
    
    def __init__(self, nome):
        self.nome = nome
        self.estado = 'Desativado'
    
    
    def get_dict_info(self):
        return {'nome': self.nome}
    
    def get_dict_all(self):
        vars(self)
    
    
    def is_activated(self):
        return True if self.estado == 'Ativado' else False
    
    
    def ativar(self):
        if not self.is_activated():
            self.estado = 'Ativado'
        else: 
            pass
    
    
    @classmethod
    def listar_restaurantes(cls):
        return cls.restaurantes_cadastrados
    
    
    @classmethod
    def adicionar(cls, restaurante):
        cls.restaurantes_cadastrados.append(restaurante.get_dict_all())
