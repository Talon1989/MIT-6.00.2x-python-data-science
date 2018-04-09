def iterativeFibonacci(n):
    num1 = 0
    num2 = 1
    for c in range(n):
        num1, num2 = num2, num1+num2
        print(num1)
    return num1

# ------------------


def retardedFibonacci(n):
    if n < 2:
        return 1
    else:
        return retardedFibonacci(n-1) + retardedFibonacci(n-2)


# MEMOIZATION


def fastFib(n, memo={}):
    """
    :param n: int >= 0
    :param memo: dictionary used by recursive calls
    :return: Fibonacci of n
    """
    if n < 2:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


# for i in range(120):
#     print(retardedFibonacci(i))




