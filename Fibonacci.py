import time
# Recursive Fibonacci Calculation
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
# Non-Recursive (Iterative) Fibonacci Calculation
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        fib_prev = 0
        fib_curr = 1
        for _ in range(2, n):
            fib_next = fib_prev + fib_curr
            sequence.append(fib_next)
            fib_prev, fib_curr = fib_curr, fib_next
        return sequence

# Take input from user
n = int(input("Enter a positive integer n: "))

# Measure time for non-recursive (iterative) calculation
start_time = time.time()
fibonacci_non_recursive = fibonacci_iterative(n)
end_time = time.time()

print("Fibonacci Sequence (Non-Recursive) up to position {n}:")
print(fibonacci_non_recursive)
print("Time taken (Non-Recursive):", end_time - start_time, "seconds")

# Measure time for recursive calculation
start_time = time.time()
fibonacci_recursive = fibonacci_recursive(n)
end_time = time.time()

print("Fibonacci Sequence (Recursive) up to position {n}:")
print(fibonacci_recursive)
print("Time taken (Recursive):", end_time - start_time, "seconds")
