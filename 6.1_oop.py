#------------------------------------------------------------------
# METHODS:
#------------------------------------------------------------------
# __init__      - constructor
#       Cannot return a value!
#       Cannot be invoked directly either from the object or from inside the class!
#
# type()        - a function to identify


#------------------------------------------------------------------
# VARIABLES:
#------------------------------------------------------------------
# __dict__      - contains the names and values of all the properties (variables) the object is currently carrying
#__name__       - contains name of the class (exists only inside classes)
#                   To find class of object use method 'type()'
# __module__    - is a string, too - it stores the name of the module which contains the definition of the class.
#                   any module named __main__ is actually not a module, but the file currently being run.
# __bases__     - is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.
#                   The order is the same as that used inside the class definition.
#                   only classes have this attribute - objects don't.
#
#

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def setSecond(self, val):
        self.second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)

# hasattr - check if object/class contains specified property
#           expects 2 arguments:
#               - class/object being checked
#               - name of property (String) whose existence has to be reported
#           Returns: True/False
if hasattr(exampleObject3, 'third'):
    print(exampleObject3.third)


# SELF - is used to:
#   - obtain access to the object's instance and class variables.
#   - invoke other object/class methods from inside the class.

print('-'*10)
# Everything we've said about property name mangling applies to method names too.
# A method whose name starts with __ is (partially) hidden.
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()


