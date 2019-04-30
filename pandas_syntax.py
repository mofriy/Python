
class mylist:

    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        a = ''
        t = 0
        for i in self.x:
            a += '{}:  {}\n'.format(t, i)
            t+=1
        return a
    
    def __lt__(self, t):
        a = []
        for i in self.x:
            if i < t:
                a.append(i)
        return (i for i in a)
    
    def __gt__(self, t):
        a = []
        for i in self.x:
            if i > t:
                a.append(i)
        return a
    
    def __eg__(self, t):
        a = []
        for i in self.x:
            if i==t:
                a.append(i)
        return a
    
    def __le__(self, t):
        a = []
        for i in self.x:
            if i <= t:
                a.append(i)
        return a
    
    def __ge__(self, t):
        a = []
        for i in self.x:
            if i >= t:
                a.append(i)
        return a
    
    def __contains__(self, x):
        if type(x)==int:
            f = False
            for i in self.x:
                if i==x:
                    f = True
            return f
        for i in x:
            f = False
            for j in self.x:
                if i==j:
                    f = True
            if f==False:
                return False
        return True
    
    def __getitem__(self, x):
        if type(x)==int:
            if x in self.x:
                return x
            return False
        a = []
        for i in x:
            if i in self:
                a.append(i)
        return a
    
b = mylist([1,3,5,7,9,11,13])
a = mylist([1,2,3,4,5,6,7,8,9,0])
print(b[a>5])
