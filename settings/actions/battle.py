from settings.characters.char import Monster
from random import randint
from settings.characters.skills.skills_object import punch

def create_monster(level):
    monster = Monster(level_monster=level)
    return monster

def battle_init(player):
    level = 18
    monster = create_monster(level)
    
    player.player_register_atacks(atack=punch)
    
    while True:
        print('Seus ataques:')
        player.print_atacks()
        x = int(input('Escolha sua ação: '))        
        action = player.use_atack(index=x)
        damage = action.damage_func(strengh=player.phisical_atack)
        monster.damage(atack=damage)
        monster_damage = monster.action_atack()
        player.damage(atack=monster_damage)
        print(f'o player {player.name} level {player.level} deu {damage} de dano no inimigo')
        if monster.hp <= monster.minus_hp:
            print('o monstro morreu')
            break
        elif player.hp <= player.minus_hp:
            print('O player morreu')
            break
        print(f'a vida do monstro ficou: {monster.hp}/{monster.max_hp}')
        print(f'O monstro level {monster.level} deu {monster_damage} de dano e vc ficou com: {player.hp} de vida ')
