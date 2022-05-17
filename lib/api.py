import requests
import json
from bdb import Breakpoint
from cocktail import Cocktail

class API:
    @classmethod
    def get_all_drinks(cls):
        response_API = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail')
        cocktails = response_API.json()["drinks"]
        for cocktail in cocktails:
            Cocktail(cocktail['idDrink'], cocktail['strDrink'])
 
    def get_drink_details(cls, drink):
        response_API = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink.id}')
        cocktail = response_API.json()["drinks"][0]
        drink.instructions = cocktail['strInstructions']
        drink.glass = cocktail['strGlass']
        drink.ingredients = []
        drink.measures = []
        for attribute in cocktail.keys():

            if 'Ingredient' in attribute and cocktail[attribute] != None and cocktail[attribute] != "":
                drink.ingredients.append(cocktail[attribute])
                
            elif 'Measure' in attribute and cocktail[attribute] != None and cocktail[attribute] != "":
                drink.measures.append(cocktail[attribute])
