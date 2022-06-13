"""
Knight vs King
If you are not familiar with chess game you can learn more Here .

Here is the chess board (rows, denoted by numbers, are called ranks, columns, denoted by a letter, are called files):

alt text

You put a Knight and a King in the board.

Complete the method that tell us which one can capture the other one.

You are provided with two object array; each contains an integer (the rank, first item) and a string/char (the file, second item) to show the position of the pieces in the chess board.

Return:

"Knight" if the knight is putting the king in check,
"King" if the king is attacking the knight
"None" if none of the above occur
Example:

knight = [7, "B"], king = [6, "C"]  ---> "King"
Check the test cases and Happy coding :)
"""
def knight_vs_king (knight_position, king_position):
    if abs(knight_position[0] - king_position[0]) <= 1 and abs(ord(knight_position[1]) - ord(king_position[1])) <= 1:
        return 'King'
    if  abs(knight_position[0] - king_position[0]) == 1 and abs(ord(knight_position[1]) - ord(king_position[1])) == 2 or abs(knight_position[0] - king_position[0]) == 2 and abs(ord(knight_position[1]) - ord(king_position[1])) == 1:
        return 'Knight'
    return 'None'

def knight_vs_king_v2 (knight_position, king_position):
    dy = abs(knight_position[0] - king_position[0])
    dx = abs(ord(knight_position[1]) - ord(king_position[1]))
    if dy <= 1 and dx <= 1:
        return 'King'
    if  dy == 1 and dx == 2 or dy == 2 and dx == 1:
        return 'Knight'
    return 'None'


    
print(knight_vs_king_v2([4, "C"], [6, "D"]))
print(knight_vs_king_v2([7, "B"], [6, "C"]))
print(knight_vs_king_v2([2, "F"], [6, "B"]))

     
#print(knight_vs_king([4, "C"], [6, "D"]))
#print(knight_vs_king([7, "B"], [6, "C"]))
#print(knight_vs_king([2, "F"], [6, "B"]))






