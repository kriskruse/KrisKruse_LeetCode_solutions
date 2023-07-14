from typing import List
from timeit import timeit


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return len(nums[:i])
    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return len(nums) - i

if __name__ == '__main__':
    l1 = [3, 2, 2, 3]
    t1 = Solution().removeElement(l1, 3)
    t2 = Solution().removeElement2(l1, 3)
    if t1 != t2:
        print(f"Solution from removeElement: {t1}")
        print(f"Solution from removeElement2: {t2}")
        print("Wrong")
        exit(200)


    print(timeit("Solution().removeElement([3, 2, 2, 3], 3)", setup="from __main__ import Solution", number=100000))
    print(timeit("Solution().removeElement2([3, 2, 2, 3], 3)", setup="from __main__ import Solution", number=100000))


