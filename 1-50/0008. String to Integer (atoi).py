class Solution:
    def myAtoi(self, str: str) -> int:
        if str == '':
            return 0
        len_s = len(str)
        # 返回值
        myAtoi = 0
        # 下标
        i = 0
        # 负数计数器
        minus = 1

        # 去除空格
        while i < len_s:
            if ord(str[i]) != 32:
                break
            else:
                i = i + 1

        # 全是空格 i溢出
        if i == len_s:
            return 0

        # 不是空格的这个字符
        # 有可能是数字/正负/其他字符
        # 所以分成三种情况讨论
        # 一开始就是其他字符直接返回
        # 正负
        if ord(str[i]) == 43:
            minus = 1
        elif ord(str[i]) == 45:
            minus = -1
        #其他字符
        elif ord(str[i]) > 57 or ord(str[i]) < 48:
            return 0
        else:
            myAtoi = int(str[i])

        # 接下来处理剩下的字符
        # 如果不是数字直接返回当前的数字
        # *返回之前需要判断溢出
        i = i + 1
        while i < len_s and 47 < ord(str[i]) < 58:
            myAtoi = myAtoi * 10 + int(str[i])
            i = i + 1



        # 判断溢出以及输出
        myAtoi = myAtoi * minus
        if myAtoi >= pow(2,31) - 1:
            myAtoi = pow(2,31) - 1
        elif myAtoi <= pow(-2,31):
            myAtoi = pow(-2,31)
        return myAtoi


s1 = "   -42"
s2 = "4193 with words"
s3 = "words and 987"
s4 = "-91283472332"
A=Solution()
print(A.myAtoi(s1))
print(A.myAtoi(s2))
print(A.myAtoi(s3))
print(A.myAtoi(s4))
print(A.myAtoi(''))