from collections import OrderedDict

class Base(object):
    #age = 10
    def __del__(self):
        self._age = 20
        #print("In delete")
        #print("Age  %s " % self.age)

    def __init__(self, name=None, age=None):
        self.name = name
        self._age = age
        print(self._age)

    @classmethod
    def check_max_age(cls):
        M = Base()
        #print(M.age)
        print(Base._age)

    @staticmethod
    def check_small_age():
        Base._age = [1,2,3,4]
        print(Base._age)
"""
        for c in cls(age):
            print(c)
        dic = OrderedDict()
        print(dic)
    @staticmethod
    def check_small_age():
        for c in age:
            print(c)
"""
Base('Puneet', [23,12,45,1,100])
Base.check_small_age()
Base.check_max_age()
#b.check_small_age()