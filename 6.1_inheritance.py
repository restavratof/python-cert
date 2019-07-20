class Star1:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

class Star2:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun1 = Star1("Sun", "Milky Way")
print(sun1)
sun2 = Star2("Sun", "Milky Way")
print(sun2)


# --- issubclass
# each class is considered to be a subclass of itself.
# issubclass(ClassOne, ClassTwo)
#         The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.

# --- isinstance
# isinstance(objectName, ClassName)
#       The functions returns True if the object is an instance of the class, or False otherwise


# --- is
#   objectOne is objectTwo
#       The is operator checks whether two variables (objectOne and objectTwo here) refer to the same object.


# --- super()
#       Accesses the superclass without needing to know its name
#       The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked
#       Invoke the superclass constructor, but also to get access to any of the resources available inside the superclass
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Andy")
print(obj)


# We can say that Python looks for object components in the following order:
#     1. Inside the object itself;
#     2. In its superclasses, from bottom to top;
#     3. If there is more than one class on a particular inheritance path, Python scans them from left to right.



# --- POLYMORPHISM
class One:
    def doit(self):
        print("doit from One")

    def doanything(self):
        self.doit()

class Two(One):
    def doit(self):
        print("doit from Two")

one = One()
two = Two()

one.doanything()
two.doanything()


# --- MRO stands for Method Resolution Order
#       this is the algorithm Python uses to look up the inheritance tree in order to find the needed methods.




