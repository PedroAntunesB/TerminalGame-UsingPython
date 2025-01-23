from settings.actions.battle import battle_init
from settings.characters.inventario import Inventario

def mostrar_inventario(player):
    inventario = Inventario()
    inventario.mostrar_inventario()
    return init_action(player)
    
        
def olhar_status(player):
    print(f'\n{player}')
    return init_action(player)


def init_action(player):
    print('\nescolha uma das opções de ação:')
    print('1-Abrir inventario\n2-Batalha\n3-Olhar Status')
    while True:
        choice = int(input('Sua escolha: '))
        if choice == 1:
            return mostrar_inventario(player)
        elif choice == 2:
            return battle_init(player)
        elif choice == 3:
            return olhar_status(player)
