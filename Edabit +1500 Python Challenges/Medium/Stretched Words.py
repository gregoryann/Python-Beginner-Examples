"""
Stretched Words

Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.

Examples
unstretch("ppoeemm") ➞ "poem"

unstretch("wiiiinnnnd") ➞ "wind"

unstretch("ttiiitllleeee") ➞ "title"

unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"

Notes
Final strings won't include words with double letters (e.g. "passing", "lottery").
"""



################################################################
"""
Solution 1
"""


def unstretch(word):
  return word[0] + ''.join(word[i] for i in range(1,len(word)) if word[i] != word[i-1])



################################################################
"""
Solution 2
"""


def unstretch(word):
	ret = [word[0]]
	for i in range(1,len(word)):
		if word[i]!=word[i-1]:
			ret.append(word[i])
	return ''.join(ret)



################################################################
"""
Solution 3
"""


def unstretch(word):
    lis = list(word)
    i=0
    j=1
    while j <len(lis):
        if lis[i]==lis[j]:
            lis.pop(j)
            j=i+1
        else:
            i +=1
            j +=1
    result=''
    for char in lis:
        result +=char
    return result




#################################################################
"""
Solution 4
"""


def unstretch(word):
	lis = []
	j=0
	for i in range(len(word)):
		if i <= (len(word)-2):
			if word[i]!=word[i+1]:
				lis.append(set(word[j:i+1]))
				j = i+1
			else:
				pass
		else:
			lis.append(set(word[j:]))
	lis = [x for i in lis for x in i]
	return "".join(lis)



