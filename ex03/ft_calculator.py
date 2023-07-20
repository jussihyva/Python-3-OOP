class calculator:
    '''
A calculator class that do calculations (addition, multiplication, subtraction, division) of vector with a scalar.
    '''
    def __init__(self, vector:list) -> None:
        self.vector:list = vector

    def __add__(self, object) -> None:
        self.vector:list = list(map(lambda x: x + object, self.vector))
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector:list = list(map(lambda x: x * object, self.vector))
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector:list = list(map(lambda x: x - object, self.vector))
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            self.vector:list = list(map(lambda x: x / object, self.vector))
            print(self.vector)
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, str(e)))
