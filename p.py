# Function to multiply n and m using one iteration
def multiply_one_iteration(n, m):
    return n * m

# Function to multiply n and m using n iterations
def multiply_n_iterations(n, m):
    result = 0
    for _ in range(n):
        result += m
    return result

# Example usage
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

# Calling both functions
result_one_iteration = multiply_one_iteration(n, m)
result_n_iterations = multiply_n_iterations(n, m)

print(f"Multiplication using one iteration: {result_one_iteration}")
print(f"Multiplication using n iterations: {result_n_iterations}")
