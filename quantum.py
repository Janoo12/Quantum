from random import randrange
from matrix import *
import sys
sys.path.insert(0, '../qworld/include/')
from drawing import draw_axes, draw_unit_circle, draw_quantum_state, draw_qubit, draw_qubit_grover, show_plt
from quantum_state import random_qstate_by_value, random_qstate_by_angle, angle_qstate
from grover import giant_oracle, giant_oracle2, giant_diffusion, Uf, Uf_8
from math import cos, sin, pi

total=1

def s0():
    return [[1],[0]]

def s1():
    return [[0],[1]]

def rand_angle_deg():
    return randrange(3600)/10

def rand_angle_rad():
    return rand_angle_deg()/360*2*pi

def prob_selector():
    global total
    prob=round(randrange(int(total*100+1))/100,2)
    #print(prob)
    total-=prob
    return prob
    
def rand_prob_state(n):
    global total
    total=1
    return [prob_selector() if i<n-1 else round(total,2) for i in range(n)]

def rand_qstate(n_dim=2):
    return [[randrange(-1,2,2)*i**0.5] for i in rand_prob_state(n_dim)]


def check_real_qstate(v):
    return 0.98<sum([i[0]**2for i in v])<1.02

def check_complex_qstate(quantum_state):
    #print(sum([i[0].real**2+i[0].imag**2 for i in quantum_state]))
    return 0.98<sum([i[0].real**2+i[0].imag**2 for i in quantum_state])<1.02

def H():
    return [[1/2**0.5 if i*j==0 else -1/2**0.5 for i in range(2)] for j in range(2)]


def rand_qstate_by_angle(r=randrange(360)):
    return [[cos(r/360*2*pi)],[sin(r/360*2*pi)]]

def random_complex_quantum_state():
    rand = rand_qstate(4)
    #print(rand)
    return [[complex(rand[0][0],rand[1][0])],[complex(rand[2][0],rand[3][0])]]


