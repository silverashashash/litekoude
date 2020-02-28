#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (38.04%)
# Likes:    3440
# Dislikes: 188
# Total Accepted:    464.9K
# Total Submissions: 1.2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        print(dp)
        for i in range(1, len(dp)):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True

        print(dp)
        return dp[-1] 
        
    
# @lc code=end 
