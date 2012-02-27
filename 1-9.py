#Given a variable, x, that stores
#the value of any decimal number,
#write Python code that prints out
#the nearest whole number to x.

#You can assume x is not negative.

# x = 3.14159 -> 3 (not 3.0)
# x = 27.63 -> 28 (not 28.0)

x = 3.14159

#DO NOT USE IMPORT

#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

down = str(x)
up = str(x+1)

downDot = down.find('.')
upDot = up.find('.')

downRound = down[:downDot]
upRound = up[:upDot]

#floor[(i + x + (i + x + 1)) / 2 ]

#floor[(i + x + i + x + 1) / 2 ]

#floor[(2(i + x) + 1) /2 ]

#floor(i + x + 0.5)

#floor(x + x+1 / 2)
