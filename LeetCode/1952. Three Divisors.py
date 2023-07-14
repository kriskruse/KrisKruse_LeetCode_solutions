class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        div = 2
        for i in range(2, n - 1):
            if div > 3:
                return False
            if n % i == 0:
                div += 1
                i += 1
            else:
                i += 1
        return True if div == 3 else False


if __name__ == '__main__':
    from timeit import Timer

    print(Solution().isThree(2))

    print(Solution().isThree(4))

    print(Solution().isThree(12))

    t1 = Timer(
        "Solution().isThree(2)",
        "from __main__ import Solution")
    print(t1.timeit())

    t2 = Timer(
        "Solution().isThree(4)",
        "from __main__ import Solution")
    print(t2.timeit())

    t3 = Timer(
        "Solution().isThree(12)",
        "from __main__ import Solution")
    print(t3.timeit())