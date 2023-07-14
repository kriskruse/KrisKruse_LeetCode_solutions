# Check if all characters of a string have equal number of occurrences
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # u = "".join(set(s))
        # if len(u) == 1:
        #     return True
        #
        # if len(s) % len(u) != 0:
        #     return False

        # Complexity: O(n)
        dic = {}
        for i in s:
            try:
                dic[i] += 1
            except:
                dic[i] = 1

        # Complexity: O(unique characters)
        v = 0
        for i in dic:
            if v == 0:
                v = dic[i]
            if dic[i] != v:
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
