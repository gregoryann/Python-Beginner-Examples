"""
Digital Decipher

In Digital Decipher, decoding is done by the simple addition of numbers in the key and the corresponding characters on a given list. You may want to solve this challenge before proceeding further.

Create a function that takes two arguments; a positive integer and a list of integers and returns a decoded message as string.

Assign a unique number to each letter of the alphabet.

 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9  10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
 14 15 16 17 18 19 20 21 22 23 24 25 26
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:

eMessage = [20, 12, 18, 30, 21]
key = 1939

digital_decipher(eMessage, key) ➞ "scout"
Add to each obtained digit consecutive digits from the key:

  20 12 18 30 21
-  1  9  3  9  1
 ---------------
  19  3 15 21 20
Write the corresponding number against each character:

 s  c  o  u  t
19  3 15 21 20
See the below example for a better understanding:

eMessage = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
key = 1939

digital_decipher(eMessage, key) ➞ "masterpiece"

  14 10 22 29  6 27 19 18  6  12 8
-  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  13  1 19 20  5 18 16  9  5  3  5
   m  a  s  t  e  r  p  i  e  c  e

Examples
digital_decipher([20, 12, 18, 30, 21], 1939) ➞ "scout"

digital_decipher([14, 30, 11, 1, 20, 17, 18, 18], 1990) ➞ "mubashir"

digital_decipher([6, 4, 1, 3, 9, 20], 100) ➞ "edabit"
"""



################################################################
"""
Solution 1
"""


def digital_decipher(eMessage, key):
	keyPos = 0
	key = str(key)
	
	decodeMessage = ''
	for digit in eMessage:
		decodeMessage += chr(int(digit) - int(key[keyPos])+96)
		keyPos += 1
		if (keyPos >= len(key)):
		  keyPos = 0
	return decodeMessage




################################################################
"""
Solution 2
"""


def digital_decipher(eMessage, key):
	a = ' abcdefghijklmnopqrstuvwxyz'
	return ''.join(a[m-int(k)] for m, k in zip(eMessage, str(key)*100))




################################################################
"""
Solution 3
"""


def digital_decipher(eMessage, key):
	import string 
	a_z_list = list(string.ascii_lowercase)
	key_list = list(str(key))
	n = round(len(eMessage)/len(key_list))+1
	key_list = key_list*n
	result = []
	for i in range(len(eMessage)):
		code = eMessage[i] - int(key_list[i])
		index = code-1
		result.append(a_z_list[index])
	return ''.join(result)



#################################################################
"""
Solution 4
"""


def digital_decipher(eMessage, key):
    '''
    Returns eMessage deciphered with key as per the examples
    '''
    TABLE = {i:chr(ord('a')+i-1) for i in range(1,27)} # maps numbers to letters
    e_size, k_size = len(eMessage), len(str(key))
    
    # get key same size as eMessage
    key = str(key) * (e_size // k_size) + str(key)[:(e_size % k_size)]

    return ''.join(TABLE[c - int(key[i])] for i, c in enumerate(eMessage))



#################################################################
"""
Solution 5
"""


def digital_decipher(eMessage, key):
	Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
						  'g', 'h', 'i', 'j', 'k', 'l', 
						  'm', 'n', 'o', 'p', 'q', 'r', 
						  's', 't', 'u', 'v', 'w', 'x', 
						  'y', 'z']
	a = ""
	x = int(len(eMessage)/len(str(key)))
	y = len(eMessage)%len(str(key))
	key = x * str(key) + str(key)[0:y]
	for i in range(0, len(eMessage)):
		a = a + Alphabet[eMessage[i] - 1 - int(key[i])]
		
	return a




#################################################################
"""
Solution 6
"""


def digital_decipher(eMessage, key):
    secret = []
    keys = []
    index = 0

    for i in str(key):
        keys.append(int(i))

    dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
            10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
            19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

    for i in eMessage:
        if index > (len(keys) -1):
            index = 0
        x = dict[i - keys[index]]
        secret.append(x)
        index += 1
        result = ''.join(secret)
    return result