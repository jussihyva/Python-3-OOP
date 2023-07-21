class calculator:
    '''Vector calculator'''
    def  __init__(self) -> None:
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Dot product method'''
        mul_list:list = list(map(lambda x, y: float(x * y), V1, V2))
        total:float = sum(mul_list)
        print('Dot product is: {}'.format(str(total)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Addition method'''
        add_list:list = list(map(lambda x, y: float(x + y), V1, V2))
        print('Add Vector is : {}'.format(str(add_list)))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Subtraction method'''
        add_list:list = list(map(lambda x, y: float(x - y), V1, V2))
        print('Sous Vector is: {}'.format(str(add_list)))
