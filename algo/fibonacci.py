

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fib(n):
    def fib_opti(n: int, suite: list) -> int:
        if n <= 1:
            return suite[-1]
        else:
            suite.append(suite[-2] + suite[-1])
            return fib_opti(n - 1, suite)

    return fib_opti(n-1, [1, 1])

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def tests():
    TEST_RANGE = 10
    functions = {
        "basic":fibonacci,
        "reversed": fib,
        "memoization":fib_memo
    }

    for name, func in functions.items():
        for i in range(1, TEST_RANGE + 1):
            print("{}({}) = {}".format(name, i, func(i)))
        print()

if __name__ == "__main__":
    fibonacci(50)