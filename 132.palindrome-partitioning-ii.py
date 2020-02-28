#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (29.10%)
# Likes:    855
# Dislikes: 29
# Total Accepted:    120.5K
# Total Submissions: 411.9K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#

# @lc code=start
import sys
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        dp = [sys.maxsize] * (len(s) + 1)
        dp[0] = 0 
        print(dp)

        for i in range(1, len(dp)):
            for j in range(i):
                if self.is_palindrome(s[j:i + 1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        print(dp)
        return dp[-1] - 1
        


    def is_palindrome(self, s):
        return s == s[-1::-1]
                
# @lc code=end
