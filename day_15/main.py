#!/usr/bin/env python3

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'change': 5.00
            }  

def enter_coins(choice):
    print(f"Please add {MENU['espresso']['cost']:.2f}")
    quarters = int(input('Enter number of quarters: \n')) * 0.25
    dimes = int(input('Enter number of dimes: \n')) * 0.10
    nickels = int(input('Enter number of nickels: \n')) * 0.05
    pennies = int(input('Enter number of pennies: \n')) * 0.01

    total_coins = quarters + dimes + nickels + pennies

    return total_coins


while True:

    choice = input('What would you like to drink? espresso, latte, or capuccino\n')

    if choice == 'espresso':
        #TODO place this into a function
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        coins = enter_coins(choice)

        if coins >= MENU['espresso']['cost']:
            print(f'You added {coins:.2f} in change')
            resources['change'] += coins
            change = coins - MENU['espresso']['cost']
            resources['change'] -= change
            print(f'Your change is {change:.2f}')
            print(f'Here is your {choice}')

        else:
            print('You didn\'t enter enough change')

    if choice == 'report':
        print(f"Coffee {resources['coffee']}")
        print(f"Milk {resources['milk']}")
        print(f"Water {resources['water']}")
        print(f"Change: {resources['change']:.2f}")

    elif choice == 'off':
        break
