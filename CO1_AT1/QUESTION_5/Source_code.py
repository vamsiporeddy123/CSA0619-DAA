import math

def complexity(n):
    return n * (math.log2(n) ** 2)

n = int(input("Enter dataset size: "))

print("Approximate operations =", complexity(n))
print("Time Complexity = Θ(n (log n)^2)")