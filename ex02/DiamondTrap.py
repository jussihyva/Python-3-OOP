from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    '''
King 
    '''
    def set_eyes(self, eyes:str) -> None:
        self.eyes:str = eyes

    def set_hairs(self, hairs:str) -> None:
        self.hairs:str = hairs

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs
