from S1E9 import Character

class Baratheon(Character):
    '''Baratheon family member'''

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name:str = __class__.__name__
        self.eyes:str = 'brown'
        self.hairs:str = 'dark'

    def die(self) -> None:
        '''Set param is_alive to False'''
        self.is_alive:bool = False

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return 'Vector: {}'.format(tuple(super().__dict__.values()))

class Lannister(Character):

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name:str = __class__.__name__
        self.eyes:str = 'blue'
        self.hairs:str = 'light'

    def create_lannister(first_name:str, is_alive:bool):
        lannister:Lannister = Lannister(first_name, is_alive)
        return lannister

    def die(self) -> None:
        '''
Set param is_alivet to False
        '''
        self.is_alive:bool = False

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return 'Vector: {}'.format(tuple(super().__dict__.values()))
