import random

def print_pole():
    for i in range(1,5):
        for j in range(1,5):
            if pole[i][j]<10:
                print("  ",pole[i][j],"  ", end='  ')
            elif pole[i][j]<100:
                print("  ",pole[i][j],"  ", end=' ')
            elif pole[i][j]<1000:
                print("  ",pole[i][j],"  ", end='')
            else:
                print(" ",pole[i][j],"  ", end='')
        print()
    return 0

def changes():
    for i in range(1,5):
        for j in range(1,5):
            if pole[i][j] == 0:
                return True
            if pole[i][j] == pole[i-1][j] or pole[i][j] == pole[i+1][j]:
                return True
            if pole[i][j] == pole[i][j-1] or pole[i][j] == pole[i][j+1]:
                return True
    return False

def turn(pole):
    new = [[1, 1, 1, 1, 1, 1], 
           [1, 0, 0, 0, 0, 1], 
           [1, 0, 0, 0, 0, 1], 
           [1, 0, 0, 0, 0, 1], 
           [1, 0, 0, 0, 0, 1], 
           [1, 1, 1, 1, 1, 1]]
    for i in range(1,5):
        for j in range(1,5):
            new[i][j] = pole[5-j][i]
    pole = new
    return pole        

def left(pole):
    for i in range(1,5):
        for j in range(1,5):
            t = 4
            while pole[i][j] == 0 and t:
                for k in range(j,5):
                    pole[i][k] = pole[i][k+1]
                pole[i][4] = 0
                t += -1
        for j in range(1,4):
            if pole[i][j] == pole[i][j+1]:
                pole[i][j] *= 2
                #score += pole[i][j+1]
                for t in range(j+1,5):
                    pole[i][t] = pole[i][t+1]
                pole[i][4] = 0
    return pole

def down(pole):
    pole = turn(pole)
    left(pole)
    pole = turn(pole)
    pole = turn(pole)
    pole = turn(pole)
    return pole
def up(pole):
    pole = turn(pole)
    pole = turn(pole)
    pole = turn(pole)
    left(pole)
    pole = turn(pole)
    return pole

def right(pole):
    for i in range(1,5):
        for j in range(1,5):
            t = 4
            while pole[i][5-j] == 0 and t:
                for k in range(j,5):
                    pole[i][5-k] = pole[i][4-k]
                pole[i][1] = 0
                t += -1
        for j in range(1,4):
            if pole[i][5-j] == pole[i][4-j]:
                pole[i][5-j] *= 2
                #score += pole[i][j+1]
                for t in range(j+1,5):
                    pole[i][5-t] = pole[i][4-t]
                pole[i][1] = 0
    return pole
def nulls():
    coord = []
    col = 0
    for i in range(1,5):
        for j in range(1,5):
            if pole[i][j] == 0:
                coord += [(i,j)]
                col += 1
    return [coord,col]

def add_2():
    if nulls()[1] == 0:
        return 0
    if nulls()[1] < 3:
        i,j = nulls()[0][random.randint(0,nulls()[1]-1)]
        pole[i][j] = 2
        #score += 2
        return 1
    if nulls()[1] < 7:
        i,j = nulls()[0][random.randint(0,nulls()[1]-1)]
        pole[i][j] = 2
        i,j = nulls()[0][random.randint(0,nulls()[1]-1)]
        pole[i][j] = 2
        #score += 4
        return 2
    i,j = nulls()[0][random.randint(0,nulls()[1]-1)]
    pole[i][j] = 2
    i,j = nulls()[0][random.randint(0,nulls()[1]-1)] 
    pole[i][j] = 2
    i,j = nulls()[0][random.randint(0,nulls()[1]-1)]
    pole[i][j] = 4
    #score += 8
    return 3

pole = [[1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1]]

print("a = ←; d = →; w = ↑; s = ↓")
print()

add_2()
add_2()
add_2()
print_pole()
while changes():
    c = input()
    if c == 'w':
        pole = up(pole)
        add_2()
        print_pole()
    elif c == 'a':
        pole = left(pole)
        add_2()
        print_pole()
    elif c == 's':
        pole = down(pole)
        add_2()
        print_pole()
    elif c == 'd':
        pole = right(pole)
        add_2()
        print_pole()
    else:
        print("!!! Wrong answer !!!")
print("End game")