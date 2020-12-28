"""
RNA Reverse Complement

Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:

original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCUUGG"
Your function should find the complement on the right AND also reverse the resulting string.

Examples
reverse_complement("GUGU") ➞ "ACAC"

reverse_complement("UCUCG") ➞ "CGAGA"

reverse_complement("CAGGU") ➞ "ACCUG"


Notes
Assume all input seqeuences are valid.
"""




################################################################
"""
Solution 1
"""


def reverse_complement(seq):	
	return seq.translate(str.maketrans('AUGC', 'UACG'))[::-1]



################################################################
"""
Solution 2
"""


def reverse_complement(input_sequence):
    rnr = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([rnr[c] for c in input_sequence][::-1])



################################################################
"""
Solution 3
"""


def reverse_complement(input_sequence):
	myDict = {
		'A':'U',
		'C':'G',
		'G':'C',
		'U':'A'
	}
	lst = []
	for c in input_sequence:
		lst.insert(0, myDict[c])
	return ''.join(lst)




#################################################################
"""
Solution 4
"""


reverse_complement=lambda s:s.translate(str.maketrans("AUGC","UACG"))[::-1]



