from random import randrange

def print_m(M):
    [print(i) for i in M]

def dot(a,b):
    return sum([a[i]*b[i] for i in range(len(a))])

def trans(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def Mv_mult(M,u):
    return [dot(M[i],u) for i in range(len(M))]

def MM_sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))]for i in range(len(A))]

def const_mult(c,A):
    return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def MM_mult(M,N):
    return trans([Mv_mult(M,i) for i in trans(N)]) 

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

def rand_prob_op(n):
    return trans([rand_prob_state(n) for i in range(n)])

def h_adder(*args):
    result=[[] for r in range(len(args[0]))]
    [result[r].extend(i[r]) for i in args for r in range(len(args[0]))]
    #[sum(args[i]) for i in range(len(args[0]))]
    #print(args[1])
    return result
def v_adder(*args):
    result = []
    [result.extend(i) for i in args]
    return result

def tensor_x(A,B):
    #matrices=[[] for ]
    return v_adder(*[h_adder(*[const_mult(A[i][j],B) for j in range(len(A[0]))]) for i in range(len(A))])

def tensor_xm(*args):
    result = []
    [result.append(tensor_x(result[-1],args[i])) if i>0 else result.append(args[0]) for i in range(len(args))]
    return result[-1]

def eye(n):
    return [[1 if j==i else 0 for j in range(n)] for i in range(n)]

def half(M):
    #return a list of matrices with dimension nxn
    half = len(M)//2
    return [[M[h*half:(h+1)*half][0][v*half:(v+1)*half],M[h*half:(h+1)*half][1][v*half:(v+1)*half]] for h in range(2) for v in range(2)]
