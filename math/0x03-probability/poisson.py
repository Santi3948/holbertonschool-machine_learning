class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if data:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            i = 0
            aux = 0
            for item in data:
                i += 1
                aux += item
            self.lambtha = float(aux/i)
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
