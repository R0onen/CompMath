# Import necessary libraries
import numpy as np

# Define the function f(x) = e^x - 2x - 3
def f(x):
    return np.exp(x) - 2*x - 3

# Bisection Method Implementation
def bisection_method(a, b, tol=1e-6, max_iterations=1000):
    """
    Finds the root of f(x) = e^x - 2x -3 in [a, b] using the Bisection Method.
    
    Parameters:
        a (float): Lower bound of the interval.
        b (float): Upper bound of the interval.
        tol (float): Tolerance for the root accuracy.
        max_iterations (int): Maximum number of iterations.
    
    Returns:
        root (float): Approximated root.
        iterations (int): Number of iterations performed.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Function has the same sign at points a and b.")
    
    iterations = 0
    while (b - a)/2.0 > tol and iterations < max_iterations:
        c = (a + b)/2.0
        fc = f(c)
        # Debug statement to trace computation
        # print(f"Iteration {iterations}: c = {c}, f(c) = {fc}")
        if fc == 0:
            # Exact root found
            a = b = c
            break
        elif f(a) * fc < 0:
            b = c
        else:
            a = c
        iterations += 1
    root = (a + b)/2.0
    return root, iterations

# Secant Method Implementation
def secant_method(x0, x1, tol=1e-6, max_iterations=1000):
    """
    Finds the root of f(x) = e^x - 2x -3 using the Secant Method.
    
    Parameters:
        x0 (float): First initial guess.
        x1 (float): Second initial guess.
        tol (float): Tolerance for the root accuracy.
        max_iterations (int): Maximum number of iterations.
    
    Returns:
        root (float): Approximated root.
        iterations (int): Number of iterations performed.
    """
    iterations = 0
    while iterations < max_iterations:
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            raise ZeroDivisionError("Division by zero encountered in Secant Method.")
        # Compute the next approximation
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        # Debug statement to trace computation
        # print(f"Iteration {iterations}: x0 = {x0}, x1 = {x1}, x2 = {x2}, f(x2) = {f(x2)}")
        # Check for convergence
        if abs(x2 - x1) < tol:
            return x2, iterations + 1
        x0, x1 = x1, x2
        iterations += 1
    raise Exception("Secant Method did not converge within the maximum number of iterations.")

# Newton-Raphson Method for finding the exact root with high precision
def newton_raphson_method(x0, tol=1e-10, max_iterations=1000):
    """
    Finds the root of f(x) = e^x - 2x -3 using the Newton-Raphson Method.
    Used here to obtain the 'exact' root for relative error calculation.
    
    Parameters:
        x0 (float): Initial guess.
        tol (float): Tolerance for the root accuracy.
        max_iterations (int): Maximum number of iterations.
    
    Returns:
        root (float): Approximated root.
        iterations (int): Number of iterations performed.
    """
    def df(x):
        return np.exp(x) - 2  # Derivative of f(x)
    
    iterations = 0
    while iterations < max_iterations:
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. No solution found.")
        x1 = x0 - fx / dfx
        # Debug statement to trace computation
        # print(f"Iteration {iterations}: x0 = {x0}, f(x0) = {fx}, f'(x0) = {dfx}, x1 = {x1}")
        if abs(x1 - x0) < tol:
            return x1, iterations + 1
        x0 = x1
        iterations += 1
    raise Exception("Newton-Raphson Method did not converge within the maximum number of iterations.")

# Function to calculate relative error
def relative_error(approx, exact):
    """
    Calculates the relative error between the approximate and exact values.
    
    Parameters:
        approx (float): Approximated value.
        exact (float): Exact value.
    
    Returns:
        rel_error (float): Relative error.
    """
    return abs((exact - approx) / exact)

# Main function to execute methods and display results
def main():
    # Define the interval
    a = 0
    b = 2
    tol = 1e-6
    
    # Find the exact root using Newton-Raphson with high precision
    exact_root, exact_iterations = newton_raphson_method(x0=1.0, tol=1e-10)
    print(f"Exact root (using Newton-Raphson): {exact_root:.10f} (found in {exact_iterations} iterations)")
    
    # Bisection Method
    try:
        bisection_root, bisection_iterations = bisection_method(a, b, tol)
        print(f"Bisection Method: Root = {bisection_root:.10f}, Iterations = {bisection_iterations}")
        # Calculate relative error
        bisection_rel_error = relative_error(bisection_root, exact_root)
        print(f"Bisection Method: Relative Error = {bisection_rel_error:.10f}")
    except ValueError as ve:
        print(f"Bisection Method Error: {ve}")
    except Exception as e:
        print(f"Bisection Method Error: {e}")
    
    print()  # For better readability
    
    # Secant Method
    # Initial guesses for Secant Method can be chosen based on the interval
    x0 = 0
    x1 = 2
    try:
        secant_root, secant_iterations = secant_method(x0, x1, tol)
        print(f"Secant Method: Root = {secant_root:.10f}, Iterations = {secant_iterations}")
        # Calculate relative error
        secant_rel_error = relative_error(secant_root, exact_root)
        print(f"Secant Method: Relative Error = {secant_rel_error:.10f}")
    except ZeroDivisionError as zde:
        print(f"Secant Method Error: {zde}")
    except Exception as e:
        print(f"Secant Method Error: {e}")

if __name__ == "__main__":
    main()