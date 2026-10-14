class MyClass:

    #Class variables / attribute
    var1 ="Mirel Fernandes"
    var2 = "abc"
    dynamic_var = "Dynamic Variable"

    #Instance variables --> defined at the time of instance
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1 #Public
        self.__dyn2= dyn2 #Private
        self._dyn3 = dyn3 #Protected

    #Methods
    def func1(self):
        print(f"Hello World , {self.dyn1} ")

    def func2(self):
        print(f"Hello Globe , {self.__dyn2}")

    def func3(self):
        print(f"Hello Globe , {self._dyn3}")


#Python Object 
obj1 = MyClass('a','b','c')
obj1.func2()
#print(obj1.dyn1 , obj1.dyn2) #AttributeError: 'MyClass' object has no attribute 'dyn2'. Did you mean: 'dyn1'?

# But now if i assign values to the variable

obj1.dyn2 = 'abc' #it should have created a new variable in the object class as dyn2 and assign to it
print(obj1.dyn2) #it will print abc but not assign to __dyn2
#print(obj1.__dyn2) #AttributeError: 'MyClass' object has no attribute '__dyn2'. Did you mean: '_MyClass__dyn2'?
obj1.func2()

obj1._dyn3 = 'cde' 
print(obj1._dyn3) #it will print abc but not assign to _dyn3
obj1.func3()
