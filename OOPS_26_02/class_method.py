class MyClass():

    class_variable = 2

    def __init__(self,value):
        self.instance_variable = value

# classmethod(function) -> method

# Convert a function to be a class method.

# A class method receives the class as implicit first argument,
# just like an instance method receives the instance.
# To declare a class method, use this idiom:

#   class C:  
#       @classmethod  
#       def f(cls, arg1, arg2, argN):  
#           ...


    @classmethod
    def class_method(cls,number):
        cls.class_variable += number
        return cls.class_variable
    
print(MyClass.class_method(3)) # 2 + 3 = 5
print(MyClass.class_method(7)) # 5 + 7 = 12


class ChildClass(MyClass):

    def __init__(self):
        MyClass.__init__(self,5)

    @classmethod
    def class_method(cls):
        print("I am in Child Class")

child_1 = ChildClass()
child_1.class_method()

ChildClass.class_method()