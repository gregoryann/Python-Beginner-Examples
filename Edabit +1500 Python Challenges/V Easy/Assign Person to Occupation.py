"""
Assign Person to Occupation
You have two lists. One shows the names of the people, while the other shows their occupation. Your task is to make a dictionary displaying each person to their respective occupations.

Person	Job
Annie	Teacher
Steven	Engineer
Lisa	Doctor
Osman	Cashier

Notes
Check the Resources tab for some useful information that can help you with this challenge.
"""


"""
Solution 1
"""

def assign_person_to_job(pl, jl):
	return {p:j for p,j in zip(pl,jl)}

"""
Solution 2
"""

def assign_person_to_job(people, jobs):
	return {person: job for person, job in zip(people, jobs)}

"""
Solution 3
"""

pl = ["Annie", "Steven", "Lisa", "Osman"]
jl = ["Teacher", "Engineer", "Doctor", "Cashier"]
def assign_person_to_job(pl, jl):
		return dict(zip(pl, jl))

"""
Solution 4
"""

def assign_person_to_job(pl, jl):
	dic = {}
	for i in range(len(pl)):
		dic[pl[i]]=jl[i]
	return dic




