import random
#у меня данных с лаб. работ нету, поэтому так
f = open('data.txt', 'w')
for i in range(500):
    j = random.random()*500
    f.write(str(j) + '\n')
