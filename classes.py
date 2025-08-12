class Restaurante:
    nome: str
    categoria: str
    estado: str
    restaurantes_cadastrados = []
    
    
    def __init__(self, nome, categoria, estado='Desativado'):
        self.nome = nome
        self.categoria = categoria
        self.estado = estado
    
    
    def get_dict_info(self):
        return {key: value for key, value in vars(self).items() if key != 'estado'}
    
    
    def get_dict_all(self):
        return vars(self)
    
    
    def is_activated(self):
        return True if self.estado == 'Ativado' else False
    
    
    def mudar_estado(self):
        self.estado = 'Desativado' if self.is_activated() else 'Ativado'
            
            
    @classmethod
    def atualizar_estado(cls, escolha, novo_estado):
        cls.restaurantes_cadastrados[escolha - 1]['estado'] = novo_estado
    
    
    @classmethod
    def retornar_lista(cls):
        return cls.restaurantes_cadastrados
    
    
    @classmethod
    def adicionar(cls, restaurante):
        cls.restaurantes_cadastrados.append(restaurante.get_dict_all())
 