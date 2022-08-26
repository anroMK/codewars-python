# Deodorant Evaporator

# Problem

This program tests the life of an evaporator containing a gas.

We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. All numbers are strictly positive.

The program reports the nth day (as an integer) on which the evaporator will be out of use.

[codewars](https://www.codewars.com/kata/5506b230a11c0aeab3000c1f)
### Example:
```
evaporator(10, 10, 5) -> 29
```
### Note:
Content is in fact not necessary in the body of the function "evaporator", you can use it or not use it, as you wish. Some people might prefer to reason with content, some other with percentages only. It's up to you but you must keep it as a parameter because the tests have it as an argument.

### Solution
```python
def evaporator(content, evap_per_day, threshold):
    day = 0
    current_content = content
    min_content = content * threshold/100
    while current_content > min_content:
        current_content -= (evap_per_day/100*current_content)
        day += 1
        #print(f"day {day}")
    return day
```

### Test
```python
print(evaporator(10,10,5))
```