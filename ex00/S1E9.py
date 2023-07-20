from abc import ABC, abstractmethod


class Character(ABC):
    '''
An abstract class which can take a first_name as first parameter, 
is_alive as second non mandatory parameter set to True by default and 
can change the health state of the character with a method that passes is_alive from True to False.
    '''
    @abstractmethod
    def __init__(self, first_name:str, is_alive:bool=True) -> None:
        self.first_name:str = first_name
        self.is_alive:str = is_alive
        self.family_name:str = self.__class__.__name__

    @abstractmethod
    def die(self, is_alive:bool) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Stark(Character):
    '''
A class (Stark) which can take a first_name as first parameter, 
is_alive as second non mandatory parameter set to True by default and 
can change the health state of the character with a method that passes is_alive from True to False.
    '''
    def __init__(self, first_name:str, is_alive:bool=True) -> None:
        '''
Initialize a class (Stark)
        '''
        self.first_name:str = first_name
        self.is_alive:str = is_alive

    def die(self) -> None:
        '''
Set param is_alivet to False
        '''
        self.is_alive:bool = False
