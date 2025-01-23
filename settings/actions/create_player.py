from settings.characters.char import Player
from settings.characters.classes_player import esc_class
def start():
    name = str(input('Escreva o nome do jogador:'))
    print('1- Barbaro\t2- Mago\t3-Assassino')
    player_class = int(input('Escolha uma classe: '))
    return create_player(name, player_class)


def create_player(player_name,player_class):
    creating_player = Player(name=player_name, player_class=player_class)
    esc_class(player_class, creating_player)

    return creating_player
