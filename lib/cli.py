import requests
import json
from bdb import Breakpoint
from cocktail import Cocktail


class Cli:
    def __init__(self):
        print("Best of luck!")
        # get stuff and start process

        response_API = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail')
        print(response_API.json())
        cocktails = response_API.json()["drinks"]

        
        for cocktail in cocktails:
            Cocktail(cocktail['idDrink'], cocktail['strDrink'])

        self.start()

        #print(response_API.status_code)

    def start(self):
        print('I am here')

        
        
    def print_cocktails(self):
            for idx, cocktail in enumerate(Cocktail.all):
                print(f'{idx}.  {cocktail.name}' )