import math

def complexity(n):
    return math.log2(n) ** 2

n = int(input("Enter number of user queries: "))

print("Approximate operations =", round(complexity(n), 2))
print("Time Complexity = Θ((log n)^2)")