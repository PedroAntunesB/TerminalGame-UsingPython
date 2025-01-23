from settings.actions.create_player import start
from settings.actions.main_actions import init_action
try:
    player = start()
    print('Bem-vindo ao meu RPG ')
    init_action(player)
except KeyboardInterrupt:
    print('\nObrigado por jogar o meu jogo!')
except:
    print('\nUm erro inesperado aconteceu. Tente Novamente')