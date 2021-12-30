from random import randint
from tools import ssp_weapons
import time


def game():

    battle(player_weapon_selection(), enemy_weapon_selection())
    new_game()

# Player weapon selection


def player_weapon_selection():

    player_weapon_name = None

    while player_weapon_name not in list(dict.keys(ssp_weapons)):
        player_weapon_name = input('Type in you decision: paper, scissors or rock!')
        player_weapon_num = ssp_weapons.get(player_weapon_name)

    print('You chose ' + player_weapon_name)

    return player_weapon_num

# Weapon choosing for pc


def enemy_weapon_selection():

    pc_weapon_num = randint(0, 2)

    print('The enemy is choosing a weapon.')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)

    print('Your enemy chose a weapon')

    return pc_weapon_num

# Battle


def battle(pc_weapon_num, player_weapon_num):

    modulo = (pc_weapon_num - player_weapon_num) % 3

    pc_weapon_name = list(dict.keys(ssp_weapons))[pc_weapon_num]
    player_weapon_name = list(dict.keys(ssp_weapons))[player_weapon_num]

    print('ROCK!!!')
    time.sleep(2)
    print('SCISSORS!!!')
    time.sleep(2)
    print('PAPER!!!')
    time.sleep(2)

    print("The enemy's weapon is: " + pc_weapon_name)
    print("Your weapon is: " + player_weapon_name)

    time.sleep(3)

    if modulo == 1:
        print(player_weapon_name + ' beats ' + pc_weapon_name + '. You won.')
    elif modulo == 2:
        print(pc_weapon_name + ' beats ' + player_weapon_name + '. You lost')
    else:
        print(pc_weapon_name + ' equals ' + player_weapon_name + ". It's a tie.")


def new_game():

    answer = input("Wanna play again? (Y/N)")
    while answer not in ["y", "Y", "N", "n"]:
        if answer == "Y" or answer == 'y':
            game()
        elif answer == "N" or "n":
            print('End')
            exit()
