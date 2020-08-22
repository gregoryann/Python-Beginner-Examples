def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)


print count_sheeps([True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True, True,  True,  True,  True, False, False, True, True])


"""

def count_sheeps(arrayOfSheeps):
    count = 0
    for i in arrayOfSheeps:
        if i == True:
            count += 1
    return count

print count_sheeps([True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True, True,  True,  True,  True, False, False, True, True])

"""