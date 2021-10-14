# fiinding total distance between coordinates
import math

x1 = int(input('ENTER THE COORDINATE X1-:'))
y1 = int(input('ENTER THE COORDINATE Y1-:'))
x2 = int(input('ENTER THE COORDINATE X2-:'))
y2 = int(input('ENTER THE COORDINATE Y2-:'))

distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(distance)