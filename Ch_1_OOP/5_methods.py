class MyClass:

    myvar = 100

    #Dundermethod
    def __init__(self):
        print("This is an constructor method")

    def __str__(self):
        print("This is a string dunder method")


    # def change_value(self,new_value):
    #         MyClass.myvar = new_value

    #For class method instead of self use cls as industry standard
    @classmethod
    def _change_value(cls,new_value):
        cls.myvar = new_value

    #Static method no need to use self, it is independent on the class use static method and dont use self without decorator will get error
    @staticmethod
    def dummy():
        print("This is a dummy method")

#Without change_value

# obj1 = MyClass()
# obj1.myvar = 200
# print(obj1.myvar) #200
# obj2 = MyClass()
# print(obj2.myvar) #100

#Without decorator
# obj1 = MyClass()
# obj1.change_value(200) #200
# print(obj1.myvar)

# obj2 = MyClass()
# print(obj2.myvar) #200

#With decorator

obj1 = MyClass()
print(obj1.myvar)
obj1._change_value(200)
print(obj1.myvar) #200

obj2 = MyClass()
print(obj2.myvar) #200

obj3= MyClass()
print(obj3.dummy())


obj4 = MyClass()
obj4.__init__()