class calculator:
    '''
Vector calculator
    '''
    def  __init__(self) -> None:
        pass

    # @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        mul_list:list = list(map(lambda x, y: x * y, V1, V2))
        total:float = sum(mul_list)
        print('Dot product is: {}'.format(str(total)))

    def add_vec(V1: list[float], V2: list[float]) -> None:
        pass

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        pass
