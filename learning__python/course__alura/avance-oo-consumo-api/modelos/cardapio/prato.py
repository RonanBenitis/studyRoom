from modelos.cardapio.item_cardapio import ItemCardapio

'''
Nossa classe Prato herdará métodos, atributos,
de uma outra classe, no caso, ItemCardapio
'''
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        '''
        Note como conseguimos puxar o atributo com
        o nome definido na classe pai
        '''
        return self._nome