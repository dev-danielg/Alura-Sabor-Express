class Restaurante:
    _nome: str
    _categoria: str
    _estado: bool
    restaurantes_cadastrados = []
    
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._estado = False
    
    
    def to_dict(self):
        return {'nome': self.nome, 'categoria': self.categoria, 'estado': self.estado}
    
    
    @property
    def nome(self):
        return self._nome
    
    
    @property
    def categoria(self):
        return self._categoria
    
    
    @property
    def estado(self):
        return 'Ativado' if self._estado else 'Desativado'
    
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria.title()
    

    def atualizar_estado(self):
        self._estado = not self._estado
        return self._estado

   
    def listar_informacoes(self):
        informacoes = self.to_dict()
        informacoes.pop('estado')
        for indice, (key, value) in enumerate(informacoes.items(), start=1):
            print(f'{indice}. {key.title()}: {value}')
    
    
    @classmethod
    def listar_restaurantes(cls):
        restaurantes = cls.retornar_lista()
        if restaurantes:
            for indice, restaurante in enumerate(restaurantes, start=1):
                restaurante = restaurante.to_dict()
                print(f'{indice}. {restaurante['nome']}')
                restaurante.pop('nome')
                for key, value in restaurante.items():
                    print(f'{key.title()}: {value}')
            print('-' * 50)
        else:
            print('Não há restaurantes cadastrados no sistema.')
    
    
    @classmethod
    def retornar_lista(cls):
        return cls.restaurantes_cadastrados
    
    
    @classmethod
    def restaurante_existente(cls, nome):
        if cls.restaurantes_cadastrados:
            return any(restaurante.nome.upper() == nome.upper() for restaurante in cls.restaurantes_cadastrados)
        else:
            return False
    
    
    @classmethod
    def adicionar(cls, restaurante):
        cls.restaurantes_cadastrados.append(restaurante)
 