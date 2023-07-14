class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert the string to a list of integers
        # Complexity: O(n)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        l = []
        for i in s:
            l.append(alphabet.index(i) + 1)

        l = ''.join(map(str, l))
        l = list(l)
        l = map(int, l)
        l = sum(l)

        if k == 1:
            return l

        for i in range(k - 1):
            l = str(l)
            l = list(l)
            l = map(int, l)
            l = sum(l)
        return l



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
