In this project we wish to solve $-\phi'' + 4 \phi = f$ on $[0,1]$ numerically using three methods: finite difference, Pseudospectral, and Green's function, subject to Periodic Boundary Conditions (PBC). Additionally, we wish to verify empirically the orders of convergence against theory.

In general, the results boil down to differences in convergence order, where the identity function $(f(x) = x)$ and $\sin( \pi x)$ achieve convergence orders of $O(h)$ and $O(h^2)$ respectively, consistent across all three supported methods. Additionally, neither function achieves their theoretical spectral accuracy, since they lack the required smoothness.

Run `python driver.py` to reproduce the convergence tests, create plots, and print errors. See `writeup/Writeup.pdf` for derivations of the analytical solution(s), error tables, and discussion about the results.
