from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first_name:str, is_alive:bool=True) -> None:
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name:str, is_alive:bool=True) -> None:
        super().__init__(first_name, is_alive)
        self.first_name:str = first_name
        self.is_alive:str = is_alive
