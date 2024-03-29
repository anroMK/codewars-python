# Monty Hall Problem
## Problem

The Monty Hall problem is a probability puzzle base on the American TV show "Let's Make A Deal".

In this show, you would be presented with 3 doors: One with a prize behind it, and two without (represented with goats).

After choosing a door, the host would open one of the other two doors which didn't include a prize, and having been shown a false door, however the math proves that you significantly increase your chances, from 1/3 to 2/3 by switching.ask the participant if he or she wanted to switch to the third door. Most wouldn't. One would think you have a fifty-fifty chance of winning after

Further information about this puzzle can be found on https://en.wikipedia.org/wiki/Monty_Hall_problem.

In this program you are given an array of people who have all guessed on a door from 1-3, as well as given the door which includes the price. You need to make every person switch to the other door, and increase their chances of winning. Return the win percentage (as a rounded int) of all participants.

[codewars](https://www.codewars.com/kata/54f9cba3c417224c63000872)

### Solution
```python
def monty_hall(correct_door_number, participant_guesses):
    return round(len([x for x in participant_guesses if x != correct_door_number]) / len(participant_guesses)*100)
```

### Test
```python
print(monty_hall(2, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]))
```