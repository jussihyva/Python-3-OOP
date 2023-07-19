from abc import ABC, abstractmethod


class Character(ABC):
    '''
An abstract class which can take a first_name as first parameter, 
is_alive as second non mandatory parameter set to True by default and 
can change the health state of the character with a method that passes is_alive from True to False.
    '''
    eyes:str = 'brown'
    hairs:str = 'dark'

    def __init__(self, first_name:str, is_alive:bool=True) -> None:
        pass

    @abstractmethod
    def die(self, is_alive:bool) -> None:
        pass

    def __str__(self) -> str:
        return 'Vector: {}'.format(self.__dict__.values())

    def __repr__(self) -> str:
        return 'Vector: {}'.format(self.__dict__.values())


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

    def AAAA(self, is_alive:bool) -> None:
        self.is_alive:bool = is_alive
