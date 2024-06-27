# class Robot:                      #Parent class
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("Hi, I am " + self.name)

# class PhysicianRobot(Robot):     #Derived class
#     pass

# x = Robot("Marvin")
# y = PhysicianRobot("James")
# print(x, type(x))
# print(y, type(y))

# y.say_hi()                        #Inherited method invocation



# # base class
# class Animal:
    
#     def eat(self):
#         print( "I can eat!")
    
#     def sleep(self):
#         print("I can sleep!")

# # derived class
# class Dog(Animal):
    
#     def bark(self):
#         print("I can bark! Woof woof!!")

# # Create object of the Dog class
# dog1 = Dog()

# # Calling members of the base class
# dog1.eat()
# dog1.sleep()

# # Calling member of the derived class
# dog1.bark()


# # Overriding

# class Robot:
#     def __init__(self, name):
#         self.name = name

#     def say_hi(self):
#         print("Hi, I am " + self.name)

# class PhysicianRobot(Robot):
#     def say_hi(self):
#         print("Everything will be okay! ")
#         print(self.name + " takes care of you!")        # y.say_hi() invokes the overridden method
    
# y = PhysicianRobot("James")
# y.say_hi() 


# # Accessing Overridden Methods

# y = PhysicianRobot("Doc James")
# y.say_hi()
# print("... and now the 'traditional' robot way of saying hi :-)")
# Robot.say_hi(y) 



# # Multiple Inheritance

# class Robot:
#  def __init__(self, name):
#     self.name = name

#  def say_hi(self):
#     print("Hi, I am " + self.name)

# class Pysician:
#  def __init__(self, specialization):
#     self.specialization = specialization

#  def print_specialization(self):
#     print("My specialization is " + self.specialization)


# class PhysicianRobot(Robot, Pysician):
#  def __init__(self, name, specialization):
#     Robot.__init__(self, name)
#     Pysician.__init__(self, specialization)

#  def say_hi(self):
#     print("Everything will be okay! ")
#     print(self.name + " takes care of you!")

# y = PhysicianRobot("James", "Cardiovascular medicine")
# y.say_hi()
# y.print_specialization() 


# # Diamond Problem

# class A:
#     def m(self): 
#         print("m of A called")
# class B(A):
#     def m(self):
#         print("m of B called")
# class C(A):
#     def m(self):
#         print("m of C called")
# class D(B,C):
#     pass


