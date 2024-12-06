if __name__ == '__main__':
    pass


# retour des dix zero 
def several_zeros():
    return [0] * 10

if __name__ == '__main__':
    print(several_zeros())




# retour dun nombre de zero par defaut
def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros


if __name__ == '__main__':
    print(several_zeros_custom())  
    print(several_zeros_custom(5))     


def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]



# return de row et col de zeros
if __name__ == '__main__':
    result = matrix(2, 3)
    print(result)        
    print(result[1][2])
    print(result[0]) 



# gestion de matrix et autrres 
class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def __eq__(self, other):
        return self._matrix == other._matrix

if __name__ == '__main__':
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1.get_value(0, 1))  
    print(m1 == m2)





