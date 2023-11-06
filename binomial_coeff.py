def generate_binomial_coefficients(n):
    # Create a 2D array to store binomial coefficients
    C = [[0] * (n + 1) for _ in range(n + 1)]

    # Calculate binomial coefficients using dynamic programming
    for i in range(n + 1):
        for j in range(min(i, n) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C

def print_binomial_coefficients(C):
    n = len(C) - 1
    for i in range(n + 1):
        for j in range(i + 1):
            print(C[i][j], end=" ")
        print()

# Input for the number of rows in Pascal's Triangle
n = int(input("Enter the number of rows for Pascal's Triangle: "))

binomial_coefficients = generate_binomial_coefficients(n)
print("Binomial Coefficients (Pascal's Triangle):")
print_binomial_coefficients(binomial_coefficients)
