
from cmath import exp
from math import pi
from math import sqrt

def dft(l):
    return [1/sqrt(len(l))*sum([exp(2j*pi*j*k/len(l))*i for j,i in enumerate(l)]) for k in range(len(l))]
