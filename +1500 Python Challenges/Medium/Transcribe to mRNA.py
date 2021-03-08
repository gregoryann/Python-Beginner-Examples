"""
Transcribe to mRNA

Transcribe the given DNA strand into corresponding mRNA - a type of RNA, that will be formed from it after transcription. DNA has the bases A, T, G and C, while RNA converts to U, A, C and G respectively.

Examples
dna_to_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"

dna_to_rna("CGATATA") ➞ "GCUAUAU"

dna_to_rna("GTCATACGACGTA") ➞ "CAGUAUGCUGCAU"

Notes
Transcription is the process of making complementary strand.
A, T, G and C in DNA converts to U, A, C and G respectively, when in mRNA.
"""




################################################################
"""
Solution 1
"""


def dna_to_rna (dna):
	return dna.translate(str.maketrans('ATGC', 'UACG'))



################################################################
"""
Solution 2
"""

mapping = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}

def dna_to_rna (dna):
    return ''.join([mapping[c] for c in dna])


################################################################
"""
Solution 3
"""

def dna_to_rna(dna):
	
	d_to_r = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
	
	rna = ''
	
	for gene in dna:
		rna += d_to_r[gene]
	
	return rna


#################################################################
"""
Solution 4
"""


def dna_to_rna (dna):
	return (
		dna.replace('A','U')
		.replace('T','A')
		.replace('C','X')
		.replace('G','C')
		.replace('X','G'))



#################################################################
"""
Solution 5
"""


rdna = {
    'A':'U',
    'T':'A',
    'G':'C',
    'C':'G'
}

def dna_to_rna (dna):
    return ''.join(rdna[i] for i in dna)




#################################################################
"""
Solution 6
"""


dna_to_rna=lambda d:d.translate(str.maketrans("ACGT","UGCA"))