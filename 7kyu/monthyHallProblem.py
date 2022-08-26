def monty_hall(correct_door_number, participant_guesses):
    return round(len([x for x in participant_guesses if x != correct_door_number]) / len(participant_guesses)*100)

print(monty_hall(2, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]))