  
def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

print(minutes_to_hours(120))
print(type(minutes_to_hours(120)))
print(seconds_to_hours(7200))