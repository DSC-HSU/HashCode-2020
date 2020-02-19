import math


def scurve(x, alpha, exp, max, min):
    return (max-min)/(1+(x/(alpha-x))**exp)+min


def split(numOfPart):
    alpha = 0.5
    remaining = 10000
    for i in range(numOfPart):
        part = int(remaining * scurve(alpha/numOfPart *
                                      i, alpha, math.e, alpha, 0))
        print(part)
    print(remaining)


split(5)
