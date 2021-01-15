from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:

    options = menu.get_items()
    try:

        choice = input(f'What would you like to drink? {options} ')

        if choice == 'off':
            is_on = False
        elif choice == 'report':
            my_money.report()
            coffee_maker.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                my_money.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)

    except:
        choice = input(f'What would you like to drink? {options} ')
