from S1E9 import Character

class Baratheon(Character):
    family_name:str = 'dffdsfdf'

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)
        self.first_name:str = first_name
        self.is_alive:str = is_alive

    def die(self) -> None:
        '''
Set param is_alivet to False
        '''
        self.is_alive:bool = False

    # def __str__(self) -> str:
    #     return 'Vector: {}'.format(super().__dict__.values())

    # def __repr__(self) -> str:
    #     return 'Vector: {}'.format(super().__dict__.values())

class Lannister(Character):
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        self.first_name:str = first_name
        self.is_alive:str = is_alive
        self.family_name:str = type(self).__name__
        self.eyes:str = 'brown'
        self.hairs:str = 'dark'


    # def create_lannister(self, first_name:str, is_alive:bool):
    # def create_lannister(self, first_name:str):
    def create_lannister(first_name:str, is_alive:bool):
        lannister:Lannister = Lannister(first_name, is_alive)
        # lannister:Lannister = Lannister(first_name)
        return lannister

    def die(self) -> None:
        '''
Set param is_alivet to False
        '''
        self.is_alive:bool = False
