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
        

      
          