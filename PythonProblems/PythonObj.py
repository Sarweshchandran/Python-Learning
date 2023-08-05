"""
Objects Methods
"""
'''
class Creation
'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello My Name and age  is: " +self.name, self.age)
p1 = person("Sarwesh", 20)
p1.myfunc()