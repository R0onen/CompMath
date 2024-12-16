# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the function f(x) = x^2 - 3x + 2
def f(x):
    return x**2 - 3*x + 2

# Define the derivative of f(x), f'(x) = 2x - 3
def df(x):
    return 2*x - 3

# Newton-Raphson Method Implementation
def newton_raphson(x0, tol=1e-6, max_iterations=100):
    """
    Finds the root of the function f(x) using the Newton-Raphson method.
    
    Parameters:
        x0 (float): Initial guess for the root.
        tol (float): Tolerance for convergence.
        max_iterations (int): Maximum number of iterations to perform.
    
    Returns:
        iterations_table (pd.DataFrame): Table containing iteration data.
        root (float): Approximated root.
    """
    iterations = 0
    current_guess = x0
    exact_root = None  # To be set after determining the root
    iterations_data = []
    previous_guess = None
    absolute_error = None
    relative_error = None
    
    while iterations < max_iterations:
        f_current = f(current_guess)
        df_current = df(current_guess)
        
        if df_current == 0:
            raise ZeroDivisionError(f"Derivative is zero at x = {current_guess}.")
        
        # Compute the next approximation
        next_guess = current_guess - f_current / df_current
        
        # Calculate absolute error
        if previous_guess is not None:
            absolute_error = abs(next_guess - current_guess)
            # Calculate relative error
            relative_error = absolute_error / abs(next_guess) if next_guess != 0 else None
        else:
            # For the first iteration, previous guess is not available
            absolute_error = None
            relative_error = None
        
        # Append data to the list
        iterations_data.append({
            'Iteration': iterations + 1,
            'Current Guess (x_n)': next_guess,
            'Absolute Error': absolute_error,
            'Relative Error': relative_error
        })
        
        # Check for convergence
        if absolute_error is not None and absolute_error < tol:
            root = next_guess
            break
        
        # Prepare for next iteration
        previous_guess = current_guess
        current_guess = next_guess
        iterations += 1
    else:
        # If maximum iterations reached without convergence
        root = current_guess
        print("Warning: Maximum iterations reached without convergence.")
    
    # Create a DataFrame from the iterations data
    iterations_table = pd.DataFrame(iterations_data)
    
    return iterations_table, root

# Function to plot convergence graph
def plot_convergence(iterations_table):
    """
    Plots the convergence graph of absolute error vs. iteration number.
    
    Parameters:
        iterations_table (pd.DataFrame): Table containing iteration data.
    """
    plt.figure(figsize=(8,6))
    plt.plot(iterations_table['Iteration'], iterations_table['Absolute Error'], marker='o', linestyle='-')
    plt.title('Convergence of Newton-Raphson Method')
    plt.xlabel('Iteration Number')
    plt.ylabel('Absolute Error')
    plt.yscale('log')  # Use logarithmic scale for better visibility
    plt.grid(True, which="both", ls="--")
    plt.show()

# Main function to execute the Newton-Raphson method and display results
def main():
    # Initial guess
    x0 = 2.5
    tol = 1e-6
    max_iterations = 20  # Set a reasonable maximum to prevent infinite loops
    
    # Find the exact root for relative error calculation
    # Since f(x) = x^2 - 3x + 2 factors as (x-1)(x-2), roots are x=1 and x=2
    # We'll target the root closest to the initial guess, which is x=2
    exact_root = 2.0
    
    # Perform Newton-Raphson iterations
    iterations_table, root = newton_raphson(x0, tol, max_iterations)
    
    # Calculate relative errors with respect to the exact root
    iterations_table['Relative Error (%)'] = iterations_table['Relative Error'] * 100
    
    # Display the table of iterations
    pd.set_option('display.float_format', lambda x: '%.10f' % x)
    print("Table of Iterations:")
    print(iterations_table.to_string(index=False))
    
    # Plot the convergence graph
    plot_convergence(iterations_table)
    
    # Final Results
    print(f"\nApproximated Root: {root:.10f}")
    print(f"Exact Root: {exact_root:.10f}")
    absolute_final_error = abs(root - exact_root)
    relative_final_error = (absolute_final_error / abs(exact_root)) * 100 if exact_root !=0 else None
    print(f"Final Absolute Error: {absolute_final_error:.10f}")
    print(f"Final Relative Error: {relative_final_error:.10f}%")

if __name__ == "__main__":
    main()