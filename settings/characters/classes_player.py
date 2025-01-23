def warrior_class(player):
    player.hp += (player.hp*(50/100))
    player.phisical_atack += (player.phisical_atack*(50/100))
    player.magic = 0
    player.speed -= (player.speed*(30/100))
    player.player_class = 'Barbarian'


def wizard_class(player):      
    player.hp -= (player.hp*(50/100))
    player.phisical_atack -= (player.phisical_atack*(50/100))
    player.magic += 10
    player.player_class = 'Wizard'


def assassin_class(player):  
    player.player_class = 'Assassin'
    pass


def esc_class(esc, player):
    match esc:
        case 1:
            warrior_class(player)
        case 2:
            wizard_class(player)
        case 3:
            assassin_class(player)