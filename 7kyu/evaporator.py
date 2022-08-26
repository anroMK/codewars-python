def evaporator(content, evap_per_day, threshold):
    day = 0
    current_content = content
    min_content = content * threshold/100
    while current_content > min_content:
        current_content -= (evap_per_day/100*current_content)
        day += 1
        #print(f"day {day}")
    return day
    


print(evaporator(10,10,5))

