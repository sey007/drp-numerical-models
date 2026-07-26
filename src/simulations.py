import testfunctions as func
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


#use finite difference method to solve the bvp w/ pbc
def solvepbcbvp_finitedifference(f,q):
    N = 2**q
    h = 1.0/N

    x = np.arange(N) * h
    rhs = f(x)


    n = np.arange(N)

    lam = 4 + (4 / h**2) * np.sin(np.pi * n * h)**2

    fhat = np.fft.fft(rhs)
    uhat = fhat / lam
    u = np.fft.ifft(uhat).real
    return x,u


def solvepbcbvp_pseudospectral(f,q):
    N = 2**q
    h = 1.0/N

    x = np.arange(N) * h
    rhs = f(x)
    n = np.arange(N)
    fhat = np.fft.fft(rhs)

    lam = np.zeros(N)

    for n in range(N):
        if n < N/2:
            k = n
        else:
            k = N-n

        #note that -D^2 + sigma^2I is just 4 pi^2 n^2 + 4, where n is the index 
        lam[n] = 4*(np.pi**2)*(k**2) + 4 
    
    uhat = fhat / lam
    u = np.fft.ifft(uhat).real

    return x,u




def solvepbcbvp_greensfctn(f,q):
    N = 2**q
    h = 1.0/N

    x = np.arange(N) * h
    rhs = f(x)
    n = np.arange(N)

    fhat = np.fft.fft(rhs)

    # so implementing the circulant matrix g(x,0) and then computing each entry using fft
    c = func.g(x,0)
    chat = np.fft.fft(c)
    
    uhat = h * chat * fhat

    u = np.fft.ifft(uhat).real

    return x,u



#plot results
def plot_results(f, method):                
    exact_soln = func.EXACT_SOLUTIONS[f]

    fig,axs = plt.subplots(3,2, figsize = (10,10))
    fig.suptitle(f"Method: {method.__name__} on {f.__name__}")
    for idx,q in enumerate(range(2,8)):
        x,u = method(f,q)
        
        row = idx // 2 
        col = idx % 2
        axs[row,col].plot(x,u.real, label = "numerical")
        axs[row,col].plot(x,exact_soln(x), label = "exact") 
        axs[row,col].legend()
        axs[row,col].set_title(f"q={q}, N={2**q}")

    plt.tight_layout()
    plt.show()


def print_errors(f,method):
    #compute error(s)
    exact_soln = func.EXACT_SOLUTIONS[f]
    print(f"Erros for {f} using {method}:")
    for q in range(2,8):
            x,u = method(f,q)

            phi = exact_soln(x)
            err = np.max(np.abs(phi - u))
            
            print(f"step: {q}, error: {err}")


def construct_errors(f,method):
    exact_soln = func.EXACT_SOLUTIONS[f]

    errs = []
    hs = []

    for q in range(2,8):
        x,u = method(f,q)

        phi = exact_soln(x)
        err = np.max(np.abs(phi-u))
        errs.append(err)
        hs.append(1/(2**q))

    return errs, hs

