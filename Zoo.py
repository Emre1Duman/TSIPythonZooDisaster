from abc import ABC, abstractmethod

class Zoo(ABC):

    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Zoo"


    #Methods
    @abstractmethod
    def eat(self):
        pass

    def name(self):
        pass

    def type(self):
        return self.value

class Animal(Zoo):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Animal"

    #Methods
    @abstractmethod
    def eat(self):
        pass
    

class Antelope(Animal):
     #Attributes

    #Constructors
    def __init__(self):
        self.value = "Antelope"

    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Antelope eats grass"

class BigFish(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "BigFish"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Big fish eats little fish"


class Bug(Zoo):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Bug"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Bug eats leaves"
    

class Bear(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Bear"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Bear eats big-fish, bug, chicken, cow, leaves, sheep"

class Chicken(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Chicken"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Chicken eats bug"

class Cow(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Cow"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Cow eats grass"

class Fox(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Fox"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Fox eats chicken, sheep"

class Giraffe(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Giraffe"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Giraffe eats leaves"

class Lion(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Lion"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Lion eats antelope, cow"

class Panda(Animal):
    #Attributes

    #constructors
    def __init__(self):
        self.value = "Panda"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Panda eats leaves"

class Sheep(Animal):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Sheep"

     #Methods
    def type(self):
        return self.value

    def eat(self):
        return "Sheep eats grass"



#New class for plants in the zoo
class Plant(Zoo):

#constructors
    def __init__(self):
        self.value = "Plant"

    def eat(self):
        pass

    #Methods
    def type(self):
        return self.value



class Leaves(Plant):

    def __init__(self):
        self.value = "Leaves"

    def eat(self):
        return "Consumes water"

     #Methods
    def type(self):
        return self.value


class Grass(Plant):

    def __init__(self):
        self.value = "Grass"

    def eat(self):
        return "Grass cant eat anything"

     #Methods
    def type(self):
        return self.value


 


    
    
    
