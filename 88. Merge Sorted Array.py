from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i < m:
            nums3 += nums1[i:m]
        if j < n:
            nums3 += nums2[j:n]
        nums1[:] = nums3
        print(nums1)


if __name__ == '__main__':
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)