import math

iterations = 25

def my_exp(x):
    s = 1
    t = x
    for n in range(iterations):
    	s = s + t  
    	t = t * x /(n + 2)
    return s

print(my_exp(0.125))
print(math.exp(0.125))