def solution(s, e):
    return e == s[-len(e):]


'''
def solution1(string, ending):
    x = len(ending)
    if ending == string[-x:]:
        return True
    if ending != string[-x:]:
        return False
'''

print(solution('1234567', '67'))
print(solution('1234567', '677'))


'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument 
(also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''