#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (41.05%)
# Likes:    3008
# Dislikes: 44
# Total Accepted:    225.3K
# Total Submissions: 545.8K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       # if not word1 or not word2:
       #     return 0
        dp = [[0 for i in range(len(word2)+1)]  for j in range(len(word1)+1)]
        
        for i in range(len(dp[0])):
            dp[0][i] = i 
        for j in range(len(dp)):
            dp[j][0] = j 

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] + 1, dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
        
        print(dp)
        return dp[-1][-1]




# @lc code=end
