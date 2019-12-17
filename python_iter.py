class it(object):
    def __init__(self):
        print "a"
        self.b=[1,2,3,4]
    def iter1(self):
        return iter(self.b) 

obj = it()
pp=obj.iter1()
print pp.next()
print pp.next()
print pp.next()

pp1=obj.iter1()
print pp1
