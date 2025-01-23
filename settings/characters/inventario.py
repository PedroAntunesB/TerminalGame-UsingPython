class Inventario:
    def __init__(self, espaco=[]):
        self.espaco = espaco
        
    def inventario_limite(self):
        if len(self.espaco) == 30:
            print('Inventario ja foi completamente preenchido')
            return True
        else:
            return False
    
    def armazenar_items(self, item):
        self.espaco.append(item)
    
    def mostrar_inventario(self):
        count = 1
        print('\n')
        print('Seu inventario: ')
        if len(self.espaco) == 0:
            print('você não tem nada no inventario')
        for i in self.espaco:
            print(f'item {count}:{i}')
            count += 1

    def __str__(self):
        return f'{self.espaco}'