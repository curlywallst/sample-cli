from email import message
from bdb import Breakpoint
from cocktail import Cocktail


class Cli:
    def __init__(self):
        Cocktail.get_all_drinks()
        self.start()

    def start(self):
        print('Welcome to Cocktail Corner - A place to discover delicious new drinks to try!')
        print(' ')
        print('Choose a drink from the list below:')
        print(' ')

        while True:
            self.print_cocktails()
            print(' ')

            pick = self.ask_user()
            if pick == 'exit':
                break

            drink = Cocktail.all[int(pick) - 1]
            print(drink.name)
            print("Yum - great choice!")
            print(' ')
            print(f'Mixing your {drink.name} now!')
            print(' ')
            if not hasattr(drink, 'instructions'):
                Cocktail.get_drink_details(Cocktail, drink)
            # print details
            print(drink.instructions)
            print(' ')
            message = 'Would you like to see another delicious drink? (y/n):   '    
            pick = input(message)
            print(' ')
            if pick == 'n':
                break

        print(' ')
        print('Bye!  Drive safely!')


    def ask_user(self):  
            message = "Enter the number of your choice here:   "      
            pick = input(message)
            print(' ')
            while pick != "exit":
                if int(pick) > 0 and int(pick) <= len(Cocktail.all): 
                    return pick
                else:
                    message = "That was not an allowed choice - Please pick the number of your favorite drink:   "
                    pick = input(message)
                    print(' ')
            return pick
        
    def print_cocktails(self):
            for idx, cocktail in enumerate(Cocktail.all):
                print(f'{idx + 1}.  {cocktail.name}' )