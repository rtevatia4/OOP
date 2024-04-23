# Make fine grained interfaces that are client specific
# Client should not be forced to depend upon interface that they do not use

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run_100(self):
        pass
    
    @abstractmethod
    def run_200(self):
        pass
    
    @abstractmethod
    def wrestle(self):
        pass
    
    @abstractmethod
    def swim(self):
        pass

class Sprinter(Player):
    def run_100(self):
        print("Sprinter running 100 meters race")
    
    def run_200(self):
        print("Sprinter running 200 meters race")
    
    def wrestle(self):
        raise NotImplementedError("Sprinter does not wrestle")
    
    def swim(self):
        raise NotImplementedError("Sprinter does not swim")

class Wrestler(Player):
    def run_100(self):
        raise NotImplementedError("Wrestler does not run")
 
    def run_200(self):
        raise NotImplementedError("Wrestler does not run")
        
    def wrestle(self):
        print("Wrestler is fighting")
    
    def swim(self):
        raise NotImplementedError("Wrestler does not swim")

class Swimmer(Player):
    def run_100(self):
        raise NotImplementedError("Swimmer does not run")
 
    def run_200(self):
        raise NotImplementedError("Swimmer does not run")
        
    def wrestle(self):
        raise NotImplementedError("Swimmer does not wrestle")

    def swim(self):
        print("Swimmer swimming")

# ABove example, the base class Player provides the interface that it's subclasses must implement.
# Here by voilating the Interface segregation principle.

# To fix this issue, you should separate the interfaces into smaller 
# and more specific classes. 
# Below implmentation follows the principle

class Sprinting(ABC):
    @abstractmethod
    def run_100(self):
        pass
    
    @abstractmethod
    def run_200(self):
        pass

class Wrestling(ABC):
    @abstractmethod
    def wrestle(self):
        pass

class Swimmimg(ABC):
    @abstractmethod
    def swim(self):
        pass

class Sprinter(Sprinting):
    def run_100(self):
        print("Sprinter running 100 meters race")
    
    def run_200(self):
        print("Sprinter running 200 meters race")

class Wrestler(Wrestling):
    def wrestle(self):
        print("Wrestler is fighting")

class Swimmer(Swimmimg):
    def swim(self):
        print("Swimmer swimming")