#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.14%)
# Likes:    1593
# Dislikes: 207
# Total Accepted:    374.9K
# Total Submissions: 848.5K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
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
        #ans = nums[end]  
        ans = min(nums[start], nums[end])
        while start + 1 < end:
            mid = (start + end) // 2
            print(nums[start], nums[mid], nums[end])   
            if nums[mid] > nums[end]:
                start = mid
                ans = min(ans, nums[start])


            elif nums[mid] <= nums[end]:
                end = mid 
                ans = min(ans, nums[end])
        #    print(start, end)
        
       # print(start, end)
        return ans



        
# @lc code=end
