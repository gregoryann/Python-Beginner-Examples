"""
Planetary Weight Converter
In this challenge, you have to convert a weight weighed on a planet of the Solar System to the corresponding weight on another planet.

To convert the weight, you have to divide it by the gravitational force of the planet on which is weighed and multiply the result (the mass) for the gravitational force of the other planet. See the table below for a list of gravitational forces:

weight on planet_a / gravitational force of planet_a * gravitational force of planet_b

Planet	m/s²
Mercury	3.7
Venus	8.87
Earth	9.81
Mars	3.711
Jupiter	24.79
Saturn	10.44
Uranus	8.69
Neptune	11.15
Given a weight weighed on planet_a, return the converted value for planet_b rounded to the nearest hundredth.

Examples
space_weights("Earth", 1, "Mars") ➞ 0.38

space_weights("Earth", 1, "Jupiter") ➞ 2.53

space_weights("Earth", 1, "Neptune") ➞ 1.14
"""


##############################################################



"""
Solution 1
"""

def space_weights(planet_a, weight, planet_b):
	forces = {
    "Mercury":3.7,
    "Venus":8.87,
    "Earth":9.81,
    "Mars":3.711,
    "Jupiter":24.79,
    "Saturn":10.44,
    "Uranus":8.69,
    "Neptune":11.15
	}
	return round(weight / forces[planet_a] * forces[planet_b],2

"""
Solution 2
"""

def space_weights(planet_a, weight, planet_b):
  pl = {'Mercury':3.7,'Venus':8.87,'Earth':9.81,'Mars':3.711,'Jupiter':24.79,'Saturn':10.44,'Uranus':8.69,'Neptune':11.15}
  return round((weight/pl[planet_a]) * pl[planet_b], 2)

"""
Solution 3
"""

def space_weights(planet_a, weight, planet_b):
	dct = {"Mercury":3.7, "Venus":8.87, "Earth":9.81, "Mars":3.711, "Jupiter": 24.79, "Saturn":10.44, "Uranus":8.69, "Neptune":11.15}
	a = dct[planet_a]
	b = dct[planet_b]
	return round((b/a)* weight, 2)

"""
Solution 4
"""

def space_weights(planet_a, weight, planet_b):
  Mercury = 3.7
  Venus = 8.87
  Earth = 9.81
  Mars = 3.711
  Jupiter = 24.79
  Saturn = 10.44
  Uranus = 8.69
  Neptune = 11.15
  planet_1 = 0
  planet_2 = 0
  if planet_a.lower() == "mercury":
    planet_1 = Mercury
  elif planet_a.lower() == "venus":
    planet_1 = Venus
  elif planet_a.lower() == "earth":
    planet_1 = Earth
  elif planet_a.lower() == "mars":
    planet_1 = Mars
  elif planet_a.lower() == "jupiter":
    planet_1 = Jupiter
  elif planet_a.lower() == "saturn":
    planet_1 = Saturn
  elif planet_a.lower() == "uranus":
    planet_1 = Uranus
  elif planet_a.lower() == "neptune":
    planet_1 = Neptune
  else:
    pass
  if planet_b.lower() == "mercury":
    planet_2 = Mercury
  elif planet_b.lower() == "venus":
    planet_2 = Venus
  elif planet_b.lower() == "earth":
    planet_2 = Earth
  elif planet_b.lower() == "mars":
    planet_2 = Mars
  elif planet_b.lower() == "jupiter":
    planet_2 = Jupiter
  elif planet_b.lower() == "saturn":
    planet_2 = Saturn
  elif planet_b.lower() == "uranus":
    planet_2 = Uranus
  elif planet_b.lower() == "neptune":
    planet_2 = Neptune
  else:
    pass
  multiply = planet_2 / planet_1
  new_weight = weight * multiply
  return round(new_weight, 2)





