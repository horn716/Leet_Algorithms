# 使用动态规划解决no.5
# 制作一个len(s)*len(s)的表
# 表内元素（i,j）值=1，说明从i到j是一个回文字符串
# 优点：避免odd和even分类的情况
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #对于空字符的处理
        if s == '':
            return ''

        #最长回文
        palindrome_s = s[0]

        dp_Table = [[0 for i in range(len(s))] for i in range(len(s))]
        #处理单个字符
        for i in range(len(s)):
            dp_Table[i][i] = 1
        #处理双字符
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp_Table[i][i + 1] = 1
                palindrome_s = s[i:i + 2]
        #填写剩下的表格(三个或者以上字符)
        for k in range(2,len(s)):
            for i in range(len(s) - k):
                if s[i] == s[i + k] and dp_Table[i + 1][i + k - 1] == 1:
                    dp_Table[i][i + k] = 1
                    palindrome_s = s[i:i + k + 1]

        return palindrome_s



Temp_Str = "abcba"
A=Solution()
print(A.longestPalindrome(Temp_Str))