from typing import List


# Each unique element can appear at most twice in the array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return len(nums)
        i = 0
        for j in range(2, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 2] = nums[j]
                i += 1
        return i + 2


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
