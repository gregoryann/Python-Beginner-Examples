# Returns the secret to beautiful code
def secretToCoding1():
  print ("")
  print ("Beautiful code is both ELEGANT and EFFICIENT")
  print ("  ELEGANT: concise, easy to read, easy to understand, easy to maintain, easy to modify")
  print ("  EFFICIENT: minimal CPU operations, minimal memory/storage requirements")
  print ("")
​
​
# Returns the secret to beautiful code
def secretToCoding2():
  print ("\nBeautiful code is both ELEGANT and EFFICIENT\n  ELEGANT: short, easy to read, easy to understand, easy to maintain, easy to modify\n  EFFICIENT: minimal CPU operations, minimal memory/storage requirements\n")
​
​
# Which code is more beautiful: secretToCoding1() or secretToCoding2()?
​
​
​
import math
import random
import time
from datetime import datetime
​
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
##########
# O(1)
##########
​
# Return the name of all animals
def getAnimals():
  return animals
​
​
##########
# O(n)
##########
​
# Returns the number of animals
def countAnimals():
    num_animals = 0
    for animal in animals:
        num_animals += 1
    return num_animals
​
​
​
​
# Returns each animal with all letters lowercase
def getLowercaseAnimals():
    lowercase_animals = animals
    animal_index = 0
    for animal in animals:
        lowercase_animals[animal_index] = lowercase_animals[animal_index].lower()
        animal_index += 1
    return lowercase_animals
​
​
​
# Given the name of a animal,
# Return True if that animal is in the list, False otherwise
def hasAnimal(animal_name):
    counter = 0
    for animal in animals:
        print(counter)
        counter += 1
        if animal == animal_name:
            return True
    return False
​
​
​
​
# Given the name of a animal,
# Return the animal's index if that animal is in the list, -1 otherwise
def findAnimal(animal_name):
    animal_index = 0
    for animal in animals:
        if animal == animal_name:
            return animal_index
        animal_index += 1
    return -1
​
​
​
​
# Shuffle the order of the stored animals
def shuffleAnimals():
    num_animals = countAnimals()
    for i in range(num_animals):
        random_i = random.randrange(num_animals)
        temp_storage = animals[i]
        animals[i] = animals[random_i]
        animals[random_i] = temp_storage
​
​
​
##########
# O(n^2)
##########
​
# Print a list of all possible animal pairs
def printAnimalPairs():
    counter = 0
    for animal1 in animals:
        for animal2 in animals:
            counter += 1
            print(counter)
            print (f"{animal1} - {animal2}")
​
​
​
##########
# O(n^3)
##########
​
# Print a list of all possible animal triples
def printBookTriples():
    for animal1 in animals:
        for animal2 in animals:
            for animal3 in animals:
                print (f"{animal1} - {animal2} - {animal3}")
​
​
​
##########
# O(2^n)
##########
​
# Given a list,
# Return a list of all possible combination of animals
def getListOfAnimalCombos(l):
    list_length = len(l)
    if list_length == 0:
        return [ [] ]
    else:
        animalCombos = []
        previousCombos = getListOfAnimalCombos( l[1:] )
        for combo in previousCombos:
            animalCombos.append( combo )
            animalCombos.append( combo + [l[0]] )
        return animalCombos
​
​
​
##########
# O(n!)
##########
​
# Given a list,
# Return a list of all possible arrangements of list items
def getAllArrangements(l):
    list_length = len(l)
    if list_length <= 1:
        return [l]
    else:
        arrangements = []
        previousArrangements = getAllArrangements( l[1:] )
        for previousArrangement in previousArrangements:
            for i in range(len(previousArrangement) + 1):
                arrangements.append( previousArrangement[i:] + [l[0]] + previousArrangement[:i] )
        return arrangements
​
​
​
# Given a list,
# Return the list's length
# O(n)
def getLengthOfList(l):
    list_length = 0
    for i in l:
        list_length += 1
    return list_length
​
​
# Given a list,
# Return the list's length
# O(1)
def betterGetLengthOfList(l):
    return len(l)
​
​
# This can be used to time the runtime of various functions
def print_function_runtime():
    start_time = datetime.now()
    x = getAllArrangements(animals_11)
    # x = getAllArrangements(animals_10 + ["Kangaroo"])
    end_time = datetime.now()
    print (end_time - start_time)
​
​
# num_animals = 9
# num_arrangements = 362,880
# runtime = 1.2 seconds
​
# num_animals = 10
# num_arrangements = 3,628,800
# runtime = 9.6 seconds
​
# num_animals = 11
# num_arrangements = 39,916,800
# runtime = 2 minutes 40.7 seconds
​
​
animals_1 = ["Aardvark"]
animals_2 = ["Aardvark", "Bear"]
animals_3 = ["Aardvark", "Bear", "Cat"]
animals_4 = ["Aardvark", "Bear", "Cat", "Duck"]
animals_5 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant"]
animals_6 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo"]
animals_7 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe"]
animals_8 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo"]
animals_9 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana"]
animals_10 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]
animals_11 = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal", "Kangaroo"]
​
animals_sorted = ["Aardvark", "Bear", "Cat", "Duck", "Elephant", "Flamingo", "Giraffe", "Hippo", "Iguana", "Jackal"]