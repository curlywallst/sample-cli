import requests
import json
from bdb import Breakpoint

class Cocktail:
    all = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Cocktail.all.append(self)


    @classmethod
    def get_all_drinks(cls):
        response_API = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail')
        cocktails = response_API.json()["drinks"]
        for cocktail in cocktails:
            cls(cocktail['idDrink'], cocktail['strDrink'])
 
    def get_drink_details(cls, drink):
        response_API = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink.id}')
        cocktail = response_API.json()["drinks"][0]
        drink.instructions = cocktail['strInstructions']

    