# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:56:34 2022

@author: Archana
"""

### Importing from json to python
import json

input_file = 'C:/Users/Dell/Desktop/MachineLearning/LinearRegression/superheroes.json'
 
with open(input_file) as f:
    superHeroSquad = json.load(f)

type(superHeroSquad)
# Output: dict
superHeroSquad.keys()

### Exporting from python to json

#update secret identity of Eternal Flame
superHeroSquad['members'][2]['secretIdentity'] = 'Will Smith'

with open('superheroes.json', 'w') as file:
    json.dump(superHeroSquad, file)

### working with the Pandas Dataframe and would like to export to JSON
df.to_json('superheroes.json')

with open('superheroes.json', 'w') as file:
    json.dump(superHeroSquad, file, indent = 4)
