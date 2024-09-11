# 7.  Fibonacci Sequence Generator   
#    *Description*: Generate the first n numbers of the Fibonacci sequence.  
#    *Skills*: Loops, recursion.

def fibonacci(n):
    fibonacci_numbers = []
    a, b = 0, 1
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci_recursive(n))
