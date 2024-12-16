# Filename: task6_iteration_method.py

def f(x):
    """
    Define the function f(x) = x^2 - 6x + 5
    """
    return x**2 - 6*x + 5

def g(x):
    """
    Define the iterative function g(x) = (x^2 + 5) / 6
    Transforms the original equation x^2 - 6x + 5 = 0 into x = g(x)
    """
    return (x**2 + 5) / 6

def iteration_method(g, x0, iterations=10, true_root=1.0):
    """
    Performs the iteration method to find the root of the equation x = g(x)
    
    Parameters:
    - g: The iterative function.
    - x0: Initial guess.
    - iterations: Number of iterations to perform.
    - true_root: The actual root for error calculation.
    
    Returns:
    - A list of tuples containing iteration number, previous x, current x, and absolute error.
    """
    results = []
    prev_x = x0
    for i in range(1, iterations + 1):
        current_x = g(prev_x)
        abs_error = abs(true_root - current_x)
        results.append((i, prev_x, current_x, abs_error))
        print(f"Iteration {i}:")
        print(f"  x{i} = {current_x}")
        print(f"  Absolute Error = {abs_error}\n")
        prev_x = current_x
    return results

def plot_absolute_error(errors):
    """
    Plots the absolute error as a function of iteration number.
    
    Parameters:
    - errors: List of absolute errors after each iteration.
    """
    import matplotlib.pyplot as plt

    iterations = list(range(1, len(errors) + 1))
    plt.figure(figsize=(8,6))
    plt.plot(iterations, errors, marker='o', linestyle='-', color='blue')
    plt.title('Absolute Error vs Iteration Number')
    plt.xlabel('Iteration Number')
    plt.ylabel('Absolute Error')
    plt.grid(True)
    plt.savefig('absolute_error_plot.png')  # Save the plot as PNG
    plt.show()

def main():
    # Initial guess
    x0 = 0.5
    # True root
    true_root = 1.0
    
    # Perform iterations
    results = iteration_method(g, x0, iterations=10, true_root=true_root)
    
    # Extract errors for plotting
    errors = [result[3] for result in results]
    
    # Plot absolute error
    plot_absolute_error(errors)
    
    # Display summary
    final_result = results[-1]
    print(f"Converged to root x ≈ {final_result[2]} in {final_result[0]} iterations.")
    print(f"Absolute Error compared to true root (x = {true_root}): {final_result[3]}")

if __name__ == "__main__":
    main()