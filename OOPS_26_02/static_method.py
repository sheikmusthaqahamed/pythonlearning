class MathOperations():

    class_var = 10

    def __init__(self):
        pass

# staticmethod(function) -> method

# Convert a function to be a static method.

# A static method does not receive an implicit first argument.
# To declare a static method, use this idiom:

#      class C:  
#          @staticmethod  
#          def f(arg1, arg2, argN):  
#              ...

    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def subtract(x,y):
        return x - y
    
mathop = MathOperations()
print(MathOperations.add(5,9))  #14
print(mathop.add(5,6)) # 11

