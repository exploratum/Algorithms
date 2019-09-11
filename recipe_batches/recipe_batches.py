#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  #number of possible batches will always be < infinity
  max_possible_batches = math.inf

  for ingredient in recipe:

    #ingredient in recipe is not available in ingredients
    if not ingredients.get(ingredient):
      return 0

    #calculate possible batched for one ingredient
    batches = ingredients[ingredient] // recipe[ingredient]

    #if there are more ingredient than needed and the number of batches is the smallest so far, save it
    if batches > 0 and batches < max_possible_batches:
      max_possible_batches = batches

  #return possible values
  if max_possible_batches == math.inf:
    return 0
  else:
    return max_possible_batches




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))