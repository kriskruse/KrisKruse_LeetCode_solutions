# Check if all characters of a string have equal number of occurrences
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        val = list(count.values())
        for i in range(len(val)-1):
            if val[i] != val[i - 1]:
                return False
        return True


if __name__ == '__main__':
    from timeit import Timer
    s = Solution()
    print(s.areOccurrencesEqual('aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccc'))

    t1 = Timer(
        "Solution().areOccurrencesEqual('aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccc')",
        "from __main__ import Solution")
    print(t1.timeit())

    t2 = Timer(
        "Solution().areOccurrencesEqual('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')",
        "from __main__ import Solution")
    print(t2.timeit())

    t3 = Timer(
        "Solution().areOccurrencesEqual('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbb')",
        "from __main__ import Solution")
    print(t3.timeit())
