class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        tab = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if i < len(s) - 1 and tab[s[i]] < tab[s[i + 1]]:
                ans -= tab[s[i]]
            else:
                ans += tab[s[i]]
        return ans

if __name__ == '__main__':
    from timeit import Timer

    testlist = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    solution = [3, 4, 9, 58, 1994]
    for i in range(len(testlist)):
        if Solution().romanToInt(testlist[i]) == solution[i]:
            print(f"Testing {testlist[i]}: got expected result {True}")
        else:
            print(f"Testing {testlist[i]}: got {Solution().romanToInt(testlist[i])} Expected of {solution[i]}")


