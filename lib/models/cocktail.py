import requests
import json
from bdb import Breakpoint

class Cocktail:
    all = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Cocktail.all.append(self)


  
    