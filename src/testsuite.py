import simulations as sim
import testfunctions as fctns
import numpy as np

methods = [sim.solvepbcbvp_finitedifference, sim.solvepbcbvp_pseudospectral, sim.solvepbcbvp_greensfctn]
functions = [fctns.identity, fctns.sinpix]
Qs = [2,3,4,5,6,7]

#tests to see if each method converges properly for the functions in testfunctions.py

#a way to express what I learned to do by hand in code, it'll work for all methods
def print_pointwise_rates(errs, print_it, get_list):

    result = []
    
    for i in range(1,len(errs)):
        ratio = errs[i]/errs[i-1]

        #use the fact that err = c * h^^p for some p plus some algebra
        p = -np.log2(ratio)

        if(print_it):
            print(f"step: {i}; ratio = {ratio:.4f}; p ≈ {p:.3f}")

        if(get_list):
            result.append(p)

    if(get_list):
        return np.array(result)
            
         
#now a way to check using np.polyfit; works on finite difference but won't work on other methods
def algebraic_rate_estimate(errs, hs):
    #notice that we have err = C * h**p => log(err) = p * log(h) + log(C)
    #so we can use np.polyfit to get an estimate; this is faster b/c we use the np library directly

    log_hs = np.log(hs) 
    log_errs = np.log(errs)
    p, C = np.polyfit(log_hs, log_errs, 1)

    return p


#this time we use frequencies; works on all methods but finite difference
def spectral_rate_estimate(errs, qs):
    Ns = 2**np.array(qs)
    log_errs = np.log(errs)

    a, C = np.polyfit(Ns, log_errs,1)

    #compute sum of square residuals and total sum of squares to get R^2
    fit_vals = a * Ns + C

    ss_res = np.sum((log_errs - fit_vals)**2)
    ss_tot = np.sum((log_errs - np.mean(log_errs))**2)

    R2 = 1 - (ss_res / ss_tot)

    return a, R2



        
def run_tests():
    for f in functions:
        for method in methods: 
            errors, hs = sim.construct_errors(f, method)

            print(f"\n-- {method.__name__} on {f.__name__} --")

            print_pointwise_rates(errors, True, False)

            if method is sim.solvepbcbvp_finitedifference:
                x = algebraic_rate_estimate(errors, hs)
                print(f"Algebraic rate estimate: {x:.3f}")
            else:
                a, r2 = spectral_rate_estimate(errors, Qs)
                print(f"Spectral rate estimate: {a:.3f} (R2 = {r2:.3f}) ")

            
