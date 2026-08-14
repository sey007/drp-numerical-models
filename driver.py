import src.simulations as sim
import src.testfunctions as fctns
import src.testsuite as tests

functions_in_use = [fctns.identity, fctns.sinpix]

def main(run_tests, do_plots, print_errors):    
    if(run_tests):
        print("Running tests on convergence... \n")
        tests.run_tests()

    if(do_plots):
        print("Plotting results...")
        for method in tests.methods:
            for f in functions_in_use:
                show = input(f"Show plot of {method.__name__} on {f.__name__}? (Y/N): \n").strip().lower() == "y"

                if(show):
                    sim.plot_results(f, method)

    if(print_errors):
        for method in tests.methods:
            for f in functions_in_use:
                sim.print_errors(f, method)


if __name__ == "__main__":
    do_tests = input("Run tests? (True/False): ").strip().lower() == "true"
    do_plot = input("Do plots? (True/False): ").strip().lower() == "true"
    do_error = input("Print errors? (True/False): ").strip().lower() == "true"

    main(do_tests, do_plot, do_error)
