import numpy as np

def identity(x) : return x
def identity_exact_soln(x) :
    C1 = 1 / (8 * (1 - np.exp(2)))
    C2 = 1 / (8 * (1- np.exp(-2)))

    return C1 * np.exp(2 * x) + C2 * np.exp(-2 * x) + (x / 4.0)


def sinpix(x) : return np.sin(np.pi * x)
def sinpix_exact_soln(x) : 
    C1 = np.pi / (2 * (np.pi**2 + 4) * (np.exp(2) - 1))
    C2 = np.pi / (2 * (np.pi**2 + 4) * (1-np.exp(-2)))

    return C1 * np.exp(2 * x) + C2 * np.exp(-2 * x) + (np.sin(np.pi * x) / (np.pi**2 + 4))


def g(x,y): return (np.cosh(2 *(abs(x-y)- 0.5))) / (4 * np.sinh(1))



def step(x): 
    if(x < 0):
        return 0
    else:
        return 1

#WIP
def step_exact_soln(x):
    return 0


#just a dictionary to make retrieving exact solns for each fctn simpler
EXACT_SOLUTIONS = {identity: identity_exact_soln, sinpix: sinpix_exact_soln}
