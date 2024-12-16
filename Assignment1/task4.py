# Filename: task4_mullers_method.py
import cmath

def f(x):
    """
    Define the function f(x) = x^3 + x^2 + x + 1
    """
    return x**3 + x**2 + x + 1

def muller(f, x0, x1, x2, tol=1e-6, max_iter=100):
    """
    Implements Muller's Method to find a root of the function f.
    
    Parameters:
    - f: The function for which we are finding the root.
    - x0, x1, x2: Initial approximations.
    - tol: Tolerance for convergence.
    - max_iter: Maximum number of iterations.
    
    Returns:
    - The root found (could be complex).
    - Number of iterations performed.
    """
    for iteration in range(max_iter):
        # Calculate differences
        h0 = x1 - x0
        h1 = x2 - x1

        # Prevent division by zero
        if h0 == 0 or h1 == 0:
            raise ZeroDivisionError("Two consecutive initial guesses are identical or too close.")

        # Calculate the slopes delta0 and delta1
        delta0 = (f(x1) - f(x0)) / h0
        delta1 = (f(x2) - f(x1)) / h1

        # Calculate the coefficient 'a' in the quadratic equation
        denominator = h1 + h0
        if denominator == 0:
            raise ZeroDivisionError("Denominator in calculation of 'd' is zero.")

        d = (delta1 - delta0) / denominator

        # Quadratic coefficients
        a = d
        b = delta1 + h1 * d
        c = f(x2)

        # Calculate the discriminant
        discriminant = cmath.sqrt(b**2 - 4*a*c)

        # Choose the denominator with the larger magnitude to improve numerical stability
        if abs(b + discriminant) > abs(b - discriminant):
            denominator_new = b + discriminant
        else:
            denominator_new = b - discriminant

        # Prevent division by zero
        if denominator_new == 0:
            raise ZeroDivisionError("Denominator in calculation of dx_r is zero.")

        # Calculate the change (delta x) using Muller's formula
        dx_r = -2 * c / denominator_new
        x3 = x2 + dx_r

        # Display the current iteration and the new approximation
        print(f"Iteration {iteration+1}: x3 = {x3}")

        # Check for convergence based on the change in x
        if abs(dx_r) < tol:
            return x3, iteration+1

        # Update the points for the next iteration
        x0, x1, x2 = x1, x2, x3

    # If the method did not converge within the maximum number of iterations
    raise Exception("Muller's method did not converge within the maximum number of iterations")

# Updated initial guesses (avoiding the exact real root x = -1)
x0 = 0
x1 = 1
x2 = 2

try:
    # Find the root using Muller's Method
    root, iterations = muller(f, x0, x1, x2)
    print(f"\nRoot found: {root} in {iterations} iterations")

    # Substitute the root back into f(x) to verify
    f_x = f(root)
    print(f"\nf(x) at the found root: {f_x}")

    # Calculate the absolute error
    absolute_error = abs(f_x)
    print(f"\nAbsolute Error = {absolute_error}")

except ZeroDivisionError as zde:
    print(f"ZeroDivisionError encountered: {zde}")
except Exception as e:
    print(f"An error occurred: {e}")