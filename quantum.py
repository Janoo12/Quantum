from random import randrange

total=1

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

def rand_qstate(n_dim):
    return [[randrange(-1,2,2)*i**0.5] for i in rand_prob_state(n_dim)]


def check_qstate(v):
    return 0.98<sum([i[0]**2for i in v])<1.02

def H():
    return [[1/2**0.5 if i*j==0 else -1/2**0.5 for i in range(2)] for j in range(2)]
