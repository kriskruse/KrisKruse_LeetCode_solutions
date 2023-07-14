
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''
        for ch in s:
            res += str(ord(ch) - 96)
        res = int(res)
        for i in range(k):
            temp = 0
            while res:
                temp += res % 10
                res //= 10
            res = temp
        return res



if __name__ == '__main__':
    from timeit import Timer


    s = Solution()
    print(s.getLucky('iiii', 2))

    print(s.getLucky('leetcode', 2))

    print(s.getLucky('hvmhoasabaymnmsd', 1))

    t1 = Timer(
        "Solution().getLucky('leetcode', 2)",
        "from __main__ import Solution")
    print(t1.timeit())

    t2 = Timer(
        "Solution().getLucky('iiii', 1)",
        "from __main__ import Solution")
    print(t2.timeit())

    t3 = Timer(
        "Solution().getLucky('zbax', 2)",
        "from __main__ import Solution")
    print(t3.timeit())

    t4 = Timer(
        "Solution().getLucky('a', 1)",
        "from __main__ import Solution")
    print(t4.timeit())

