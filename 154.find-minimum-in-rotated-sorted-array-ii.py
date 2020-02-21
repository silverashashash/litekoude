#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (40.20%)
# Likes:    660
# Dislikes: 190
# Total Accepted:    159K
# Total Submissions: 395.2K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None 
        start, end = 0, len(nums) - 1
        ans = min(nums[start], nums[end])

        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] > nums[end]:
                start = mid
                ans = min(ans, nums[mid])

            elif nums[mid] < nums[end]:
                end = mid
                ans = min(ans, nums[mid])
            else:
                end -= 1 
                ans = min(ans, nums[end])

        return ans 
# @lc code=end
