from abc import ABC,abstractmethod

# #################### Musician class #################### #  

class Musician(ABC):
    '''
    An abstract class (Base/parent class) that contains instance attribute "name=> string" and abstract methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    and each child has to have them!!!
    '''
    def __init__(self,name=""):
        self.name=name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

# #################### Band class #################### #  

class Band(Musician):
    '''
    A class (child class) that contains:
        1. instance attributes "name and members"
        2. class method "to_list"
        3. class attribute "instances" which is a list of instances that inherit from base class.
        4."play_solos" method that asks each member musician to play a solo, in the order they were added to band.
        5. abstracted methods from parent class (Musician)
    '''
    instances=[]
    def __init__(self,name,members):
        super().__init__()
        self.name=name
        self.members=members
        Band.instances.append(self)
    
    def play_solos(self):
        solos=[]
        for mumber in self.members:
            solos.append(mumber.play_solo())
        return solos

    def __str__(self):
        return  self.name

    def __repr__(self):
        return self.name

    @classmethod
    def to_list(cls):
        return Band.instances
      
    def get_instrument(self):
        pass

    def play_solo(self):
        pass

# #################### Guitarist class #################### #   
 
class Guitarist(Musician):
    '''
    An class (child class) that contains instance attribute "name=> string" and abstracted methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    from parent class(Musician)
    '''
    def __init__(self,name=""):
        super().__init__()
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return"face melting guitar solo"

# #################### Bassist class #################### #  
  
class Bassist(Musician):
    '''
    An class (child class) that contains instance attribute "name=> string" and abstracted methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    from parent class(Musician)
    '''

    def __init__(self,name=""):
        super().__init__()
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

# #################### Drummer class #################### # 

class Drummer(Musician):
    '''
    An class (child class) that contains instance attribute "name=> string" and abstracted methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    from parent class(Musician)
    '''

    def __init__(self,name=""):
        super().__init__()
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


# #################### JUST FOR TESTING FROM MY SIDE  #################### # 

if __name__=="__main__":

    band1=Band("N", [Guitarist("Kurt Cobain")])
    band2=Band("A", Bassist("Krist Novoselic"))
    band3=Band("B", [])
    band4=Band("C", [
            Guitarist("Kurt Cobain"),
            Bassist("Krist Novoselic"),
            Drummer("Dave Grohl"),
        ])
    print(Band.to_list())
    print(band3.play_solos())

    the_nobodies = Band("The Nobodies", [])
    print(len(Band.instances))
    print(Band.instances[0])