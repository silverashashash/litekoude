#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (51.36%)
# Likes:    1490
# Dislikes: 100
# Total Accepted:    392.3K
# Total Submissions: 762K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_dict = {}
        if not s:
            return -1
        for char in s:
            word_dict[char] = word_dict.get(char, 0) + 1 
        
        print(word_dict)

        for char in word_dict:
            if word_dict[char] == 1:
                return s.index(char)

        return -1 
            



        
# @lc code=end
