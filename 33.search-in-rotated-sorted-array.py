#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.59%)
# Likes:    3744
# Dislikes: 406
# Total Accepted:    574.5K
# Total Submissions: 1.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1 

        while start + 1 < end:
            mid = (start + end) // 2

            if target == nums[mid]: return mid

            if target >= nums[start]:
                if target == nums[start]: return start 
                if nums[mid] > nums[start] and nums[mid] < target:
                    start = mid 
                elif nums[mid] > nums[start] and nums[mid] > target:
                    end = mid

                elif nums[mid] < nums[end]:
                    end = mid 
            
            elif target < nums[start]:
                if target == nums[end]: return end 
                if nums[mid] > nums[start]:
                    start = mid 
                elif nums[mid] < nums[end] and nums[mid] < target:
                    start = mid
                elif nums[mid] < nums[end] and nums[mid] > target:
                    end = mid 

        if nums[start] == target: return start
        if nums[end] == target: return end
        return -1





        
# @lc code=end
