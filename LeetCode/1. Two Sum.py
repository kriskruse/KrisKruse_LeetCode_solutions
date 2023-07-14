class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            if target - nums[i] in nums and i != nums.index(target - nums[i]):
                return [nums.index(target - nums[i]),i]


if __name__ == '__main__':

    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))