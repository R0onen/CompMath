# Filename: task5_false_position_method.py
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Define the function f(x) = x^2 - 2x
    """
    return x**2 - 2*x

def false_position(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Implements the False Position (Regula Falsi) method to find a root of the function f.
    
    Parameters:
    - f: The function for which the root is sought.
    - x0, x1: Initial guesses such that f(x0) and f(x1) have opposite signs.
    - tol: Tolerance for convergence.
    - max_iter: Maximum number of iterations.
    
    Returns:
    - root: The approximated root.
    - iterations: Number of iterations performed.
    - errors: List of absolute errors after each iteration.
    """
    if f(x0) * f(x1) >= 0:
        raise ValueError("Function has the same sign at the initial guesses. Choose different initial guesses.")
    
    errors = []
    for iteration in range(1, max_iter + 1):
        # Apply False Position formula to find new approximation
        x3 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        f_x3 = f(x3)
        
        # Calculate absolute error
        if iteration == 1:
            abs_error = abs(x3 - x0)
        else:
            abs_error = abs(x3 - prev_x3)
        errors.append(abs_error)
        
        # Print iteration details
        print(f"Iteration {iteration}:")
        print(f"  Approximate Root (x3) = {x3}")
        print(f"  f(x3) = {f_x3}")
        print(f"  Absolute Error = {abs_error}")
        if x3 != 0:
            rel_error = (abs_error / abs(x3)) * 100
        else:
            rel_error = 0.0
        print(f"  Relative Error = {rel_error}%\n")
        
        # Check for convergence
        if abs_error < tol:
            return x3, iteration, errors
        
        # Update the interval for next iteration
        if f(x0) * f(x3) < 0:
            x1 = x3
        else:
            x0 = x3
        
        prev_x3 = x3
    
    raise Exception("False Position method did not converge within the maximum number of iterations")

def plot_absolute_error(errors):
    """
    Plots the absolute error as a function of iteration number.
    
    Parameters:
    - errors: List of absolute errors after each iteration.
    """
    iterations = list(range(1, len(errors) + 1))
    plt.figure(figsize=(8,6))
    plt.plot(iterations, errors, marker='o', linestyle='-', color='red')
    plt.title('Absolute Error vs Iteration Number')
    plt.xlabel('Iteration Number')
    plt.ylabel('Absolute Error')
    plt.grid(True)
    plt.savefig('absolute_error_plot.png')  # Save the plot as PNG
    plt.show()

def main():
    # Initial guesses
    x0 = 1
    x1 = 3
    
    try:
        # Apply False Position method
        root, iterations, errors = false_position(f, x0, x1)
        print(f"Converged to root x = {root} in {iterations} iterations.\n")
        
        # Plot absolute error
        plot_absolute_error(errors)
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()