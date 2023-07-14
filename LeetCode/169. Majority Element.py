from typing import List
from timeit import timeit


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums: List[int]) -> int:
        li = list(set(nums))
        fq = 0
        n = 0
        for i in li:
            if nums.count(i) > fq:
                fq = nums.count(i)
                n = i
        return n

if __name__ == '__main__':
    # test if algo is correct
    l1 = [3, 2, 3]
    t1 = Solution().majorityElement(l1)
    t2 = Solution().majorityElement2(l1)
    if t1 != t2:
        print(f"Solution from majorityElement: {t1}")
        print(f"Solution from majorityElement2: {t2}")
        print("Wrong")
        exit(200)

    # test performance
    print("Test 1:")
    print(timeit("Solution().majorityElement([3, 2, 3])", setup="from __main__ import Solution", number=100000))
    print(timeit("Solution().majorityElement2([3, 2, 3])", setup="from __main__ import Solution", number=100000))

    print("Test 2:")
    print(timeit("Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])", setup="from __main__ import Solution", number=100000))
    print(timeit("Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2])", setup="from __main__ import Solution", number=100000))

    print("Test 3:")
    print(timeit("Solution().majorityElement([1, 2, 3, 4, 5, 9, 9, 9, 9, 9, 9])", setup="from __main__ import Solution", number=100000))
    print(timeit("Solution().majorityElement2([1, 2, 3, 4, 5, 9, 9, 9, 9, 9, 9])", setup="from __main__ import Solution", number=100000))