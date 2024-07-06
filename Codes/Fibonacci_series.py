# Number of terms in the Fibonacci series to be printed
n_terms = 10

# First two terms
a, b = 0, 1

# Print the first two terms separately
print(a, b, end=" ")

# Generate and print the Fibonacci sequence
for _ in range(2, n_terms):
    c = a + b
    a=b
    b=c
    print(c, end=" ")


#Output:-0 1 1 2 3 5 8 13 21 34