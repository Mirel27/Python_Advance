class MyClass:

    #Class variables / attribute
    var1 ="Mirel Fernandes"
    var2 = "abc"
    dynamic_var = "Dynamic Variable"

    #Instance variables --> defined at the time of instance
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1
        self.dyn2= dyn2
        self.dyn3 = dyn3

    #Methods
    def func1(self):
        print(f"Hello World , {self.dyn1} ")

    def func2(self):
        print(f"Hello Globe , {self.dyn2}")


#Python Object 
obj1 = MyClass('a','b','c')
obj1.func1()

#Another way to call the function
MyClass.func2(obj1)

obj1.var2 = 'changed value'
print(obj1.var2)