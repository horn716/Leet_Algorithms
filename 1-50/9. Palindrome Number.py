class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0:
            return False
        s_x = str(x)
        # odd
        if len(s_x) % 2 == 1:
            i = int(len(s_x) / 2)
            j = i
            for k in range(i):
                i = i - 1
                j = j + 1
                if s_x[i] != s_x[j]:
                    return False
        else:
            j = int(len(s_x) / 2)
            i = j - 1
            for k in range(i):
                if s_x[i] != s_x[j]:
                    return False
                i = i - 1
                j = j + 1
        return True



x1 = 12221
x2 = 1231
A = Solution()
print(A.isPalindrome(x1))
print(A.isPalindrome(x2))