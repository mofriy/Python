import random
#у меня данных с лаб. работ нету, поэтому так
f = open('data.txt', 'w')
for i in range(1000):
    t = 0
    for k in range(100):
        t += random.randint(0,1)
    f.write(str(t) + '\n')
