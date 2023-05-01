from Validator import Validator


class NumericalIntegration:

    def __init__(self, epsilon, left_border, right_border, n):
        self.__right_border = right_border
        self.__left_border = left_border
        self.__n = n
        self.__epsilon = epsilon

    def getEpsilon(self):
        return self.__epsilon

    def getN(self):
        return self.__n

    def doubleN(self):
        self.__n *= 2

    def getLeftBorder(self):
        return self.__left_border

    def getRightBorder(self):
        return self.__right_border

    def calculateMaxIteration(self, eps):
        return int(100 / eps) if eps < 1 else int(100 * eps)

    def ruleRunge(self, I_h, I_h2, k, eps):
        delta = abs(I_h2 - I_h) / (2 ** k - 1)
        print(
            f'Погрешность вычислений между значениями {I_h2} и {I_h} составляет {delta} {"<" if delta < eps else ">"} {eps}.')
        if delta <= eps:
            return True
        else:
            return False
