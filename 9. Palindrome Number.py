class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def noStrIsPalindrom(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = 0
            temp = x
            while temp > 0:
                rev = (rev * 10) + temp % 10
                temp //= 10
            return x == rev



if __name__ == '__main__':
    testlist = [121, -121, 10, -101, 123454321]
    solution = [True, False, False, False, True]
    for i in range(len(testlist)):
        if Solution().isPalindrome(testlist[i]) == solution[i]:
            print(f"Testing {testlist[i]}: got expected result {True}")
        else:
            print(f"Testing {testlist[i]}: got {Solution().isPalindrome(testlist[i])} Expected of {solution[i]}")

    for i in range(len(testlist)):
        if Solution().noStrIsPalindrom(testlist[i]) == solution[i]:
            print(f"Testing {testlist[i]}: got expected result {True}")
        else:
            print(f"Testing {testlist[i]}: got {Solution().noStrIsPalindrom(testlist[i])} Expected of {solution[i]}")