# What is Dynamic Programming (DP)?
# Dynamic Programming is a technique to solve optimization problems by breaking them into overlapping subproblems and solving each subproblem only once.
# Optimal Substructure – The solution to a problem can be built from the solution of its subproblems.
# Overlapping Subproblems – The problem involves solving the same subproblems multiple times.

# Approaches in DP

#  Memoization (Top-Down)
# You solve the problem recursively.
# Store the results in a cache (usually a dictionary or array).
# If the result is already in cache, return it instead of recomputing.

def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 1 :
        return n
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]


# Tabulation (Bottom-Up)
# You build the solution iteratively from the smallest subproblem.
# Store answers in a table/array and solve in order.

