#对于每一个（每两个）字符，在不溢出的情况下
#中心向两边扩散的搜索方式
#odd对称和even对称分开来搜索
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return  ''
        s_list = list(s)
        len_s = len(s_list)
        #最长回文计数器
        max_length = 1

        #最长回文本体
        palindrome_s = ''.join(s_list[0])

        #odd对称，i作为下标
        for i in range(len_s):
            #取左边和右边中最短的延伸长度
            max_extension = min(i,len_s - i - 1)


            #在可以延伸的范围（次数）中进行回文判断

            #初始化必要的变量
            #延伸次数count
            extension_c = 0
            #判断是否对称的左右坐标（起始点在当前下标i并且扩散一次）
            p_left = i - 1
            p_right = i + 1
            #当前位置最长回文的长度
            temp_length = 1
            while extension_c < max_extension:
                #如果左右相等，那么再延伸一次 长度加2
                #延伸计步器加一（避免溢出）
                if s_list[p_left] == s_list[p_right]:
                    temp_length = temp_length + 2
                    p_left = p_left - 1
                    p_right = p_right + 1
                    extension_c = extension_c +1
                #如果不相等直接结束while
                #并且更新最大回文
                else:
                    break
            if temp_length > max_length:
                max_length = temp_length
                palindrome_s = ''.join(s[p_left + 1 : p_right])


        #even对称，首先要判断是不是even
        #即：i和i+1下标的字母相等
        for i in range(len_s - 1):
            #even判断
            if s_list[i] == s_list[i + 1]:
                #even比odd初始多一个，少延伸一次
                max_extension = min(i, len_s - i - 2)


                # 在可以延伸的范围（次数）中进行回文判断

                # 初始化必要的变量
                # 延伸次数count
                extension_c = 0
                # 判断是否对称的左右坐标（起始点在当前下标i并且扩散一次）
                # 右边要多出一个
                p_left = i - 1
                p_right = i + 2
                # 当前位置最长回文的长度
                # 比odd多一个
                temp_length = 2
                while extension_c < max_extension:
                    #如果左右相等，那么再延伸一次 长度加2
                    #延伸计步器加一（避免溢出）
                    if s_list[p_left] == s_list[p_right]:
                        temp_length = temp_length + 2
                        p_left = p_left - 1
                        p_right = p_right + 1
                        extension_c = extension_c +1
                    #如果不相等直接结束while
                    #并且更新最大回文
                    else:
                        break
            if temp_length > max_length:
                max_length = temp_length
                palindrome_s = ''.join(s[p_left + 1 : p_right])



        return palindrome_s









Temp_Str = "ccc"
A=Solution()
print(A.longestPalindrome(Temp_Str))