#this test is inheritance in python 

class man:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name}. I am {self.age} years old.")


p = man("Mustafe", 22)

p.show()
class women:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name}. I am {self.age} years old.")


s1 = women("Alice", 25)
s2 = women("Jilli", 19)

s1.show()
s2.show()

class cat:
    def __init__(self, speak, kids):
        self.speak = speak
        self.kids = kids
        
    def show(self):
        print(f"l speak {self.speak}. l have {self.kids} only")
        
        
        
        c1 =cat("meow", 8)
        c1.show()
        
# this test it'll be class attributes
# class person:
#     number_of_people = 0  # 
    
#     def __init__(self, name):
#         self.name = name
#         person.number_of_people += 1 


# p1 = person("mustafe")
# print(person.number_of_people)
# p2 = person("imran")
# print(person.number_of_people)
# p3 = person("abdi")


# print(person.number_of_people)  

# class person:
#     number_of_people = 0  # 
    
#     def __init__(self, name):
#         self.name = name
#         person.add_person()
        
#     @classmethod
#     def number_of_people(cls):
#         return cls.number_of_people
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1 


# p1 = person("mustafe")
# p2 = person("imran")
# p3 = person("abdi")


# print(person.number_of_people_())  

# static methods
class Math:
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")

# Calling static method without an instance
Math.pr()





      
          