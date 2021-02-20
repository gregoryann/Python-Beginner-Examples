def lowest_temp(t):
    if t != '':
        return min([int(i) for i in t.split(' ')])
    else:
        return None

print(lowest_temp(''))


'''
You were given a string of integer temperature values. Create a function lowest_temp(t) and return the lowest value or
None/null/Nothing if the string is empty.
'''