"""

Enharmonic Equivalents

In music, notes can be written out in multiple ways (especially for notes on the black keys). Although these notes are spelled out differently, they still are the same note physically.

C# = Db, D# = Eb, F# = Gb, G# = Ab, A# = Bb

Given a musical note, create a function that returns its enharmonic equivalent. The examples below should make this clear.

Examples
get_equivalent("D#") ➞ "Eb"

get_equivalent("Gb") ➞ "F#"

get_equivalent("Bb") ➞"A#"

Notes
Note names will always be a capital letter followed by either # or b.
Remember that the note after G is A and vice versa.
"""




################################################################
"""
Solution 1
"""


seq = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
       
def get_equivalent(note):
    idx = seq.index(note[0])
    if '#' in note:
       return seq[idx+1] + 'b'
    else:
        return seq[idx-1] + '#'







################################################################
"""
Solution 2
"""

def get_equivalent(note):
  d = {'C#':'Db','D#':'Eb', 'F#':'Gb','G#':'Ab', 'A#':'Bb'}
  for k,v in d.items():
    if note == k:
      return v
    elif note == v:
      return k





################################################################
"""
Solution 3
"""

get_equivalent=lambda n:('CDFGA'['DEGAB'.find(n[0])]+'#','DEGAB'['CDFGA'.find(n[0])]+'b')['#'in n]








#################################################################
"""
Solution 4
"""


def get_equivalent(note):
	convert = {
		'C#':'Db',
		'Db':'C#',
		'D#':'Eb',
		'Eb':'D#',
		'F#':'Gb',
		'Gb':'F#',
		'G#':'Ab',
		'Ab':'G#',
		'A#':'Bb',
		'Bb':'A#'
	}
	return convert[note]




#################################################################
"""
Solution 5
"""


def get_equivalent(note):
	notes = ('A','B','C','D','E','F','G'); signs = ('b','#')
	i = 1 if '#' in note else -1
	return '{}{}'.format(notes[(notes.index(note[0])+i)%7],signs[signs.index(note[1])-1])
