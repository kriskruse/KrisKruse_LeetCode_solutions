from math import sqrt

class Solution:
    def isThree(self, n: int) -> bool:
        for i in range(2, int(sqrt(n))):
            if n / i == n // i:
                return False
        return sqrt(n) == int(sqrt(n)) if n != 1 else False


if __name__ == '__main__':
    from timeit import Timer

    print(Solution().isThree(2))

    print(Solution().isThree(4))

    print(Solution().isThree(12))

    t1 = Timer(
        "Solution().isThree(2)",
        "from __main__ import Solution")
    print(t1.timeit())

