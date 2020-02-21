#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.91%)
# Likes:    974
# Dislikes: 413
# Total Accepted:    210.8K
# Total Submissions: 640.6K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False 
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid 
                else:
                    end = mid - 1 
            elif nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1 
            else:
                end -=  1 

        if nums[start] == target: return True
        if nums[end] == target: return True
        return False
# @lc code=end
