  
def minutes_to_hours(minutes = 70, seconds = 3600):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(70, 300))