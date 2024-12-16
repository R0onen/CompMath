# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

# Define the function f(x) = x^3 - 2x^2 - 5
def f(x):
    return x**3 - 2*x**2 - 5

# Plotting the function in the range x ∈ [1, 4]
def plot_function():
    x = np.linspace(1, 4, 400)  # Generates 400 points between 1 and 4
    y = f(x)
    
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label='$f(x) = x^3 - 2x^2 - 5$')
    plt.axhline(0, color='black', linewidth=0.5)  # x-axis
    plt.axvline(0, color='black', linewidth=0.5)  # y-axis
    plt.title('Graph of f(x) = x³ - 2x² - 5')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Graphical method to estimate the root
def graphical_root_approximation():
    """
    From the graph, estimate the root by identifying where f(x) crosses the x-axis.
    """
    # Observing the graph between x=2 and x=3
    # Let's choose x ≈ 2.5 as an initial approximation
    return 2.5

# Calculate f(x) at the approximate root
def calculate_fx(x):
    return f(x)

# Find the true root using Newton-Raphson method for higher accuracy
def find_true_root(initial_guess):
    true_root = newton(f, initial_guess)
    return true_root

# Calculate absolute error between approximate and true root
def calculate_absolute_error(approx, true):
    return abs(true - approx)

def main():
    # Step 1: Plot the graph
    plot_function()
    
    # Step 2: Approximate root from graphical method
    approx_root = graphical_root_approximation()
    print(f"Approximate root from graphical method: x ≈ {approx_root}")
    
    # Step 3: Calculate f(x) at the approximate root
    fx_approx = calculate_fx(approx_root)
    print(f"f({approx_root}) = {fx_approx}")
    
    # Step 4: Find the true root using Newton-Raphson method
    true_root = find_true_root(approx_root)
    print(f"True root using Newton-Raphson method: x ≈ {true_root:.6f}")
    
    # Step 5: Calculate absolute error
    abs_error = calculate_absolute_error(approx_root, true_root)
    print(f"Absolute error: {abs_error:.6f}")

if __name__ == "__main__":
    main()

    