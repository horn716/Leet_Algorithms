
class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0;
        val = abs(x)
        minus = 1
        if val != x:
            minus = -1
        val_s = str(val)
        i = len(val_s) - 1
        while i >= 0:
            reverse = reverse * 10 + int(val_s[i])
            i = i - 1
        if reverse >= pow(2,31):
            reverse = 0
        return reverse * minus







x=120
A=Solution()
print(A.reverse(x))