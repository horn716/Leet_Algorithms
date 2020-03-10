# 下标递进的方式求解
# 暂时不考虑a*a这种情况


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 空集特殊状况处理
        if s == '' and p == '':
            return True
        elif s == '' and p != '':
            return self.loopOnly(p)
        elif s != '' and p == '':
            return False

        # 长度和下标
        len_s = len(s)
        len_p = len(p)
        s_index = 0
        p_index = 0
        # ismatch = False
        while s_index < len_s and p_index < len_p:
            # 等于任意字符时
            if p[p_index] == '.':
                # 任意重复
                if p_index + 1 < len_p and p[p_index + 1] == '*':
                    # 如果这个是最后一个直接通过
                    if p_index + 2 == len_p:
                        return True
                    # 由于不考虑 .*a*这种形式（a*无效）
                    # *后接至少一个非循环匹配符
                    # 故使用递归（两种考虑）
                    # 因为p_index < len_p - 1
                    # p_index + 2 != len_p
                    # 所以p_index - 2 < len_p
                    else:
                        # 第一种：.*.形式
                        # 由于下一个字符可接全类型
                        # 无法简化算法
                        # 使用最基本的递归
                        if p[p_index] == '.':
                            while s_index < len_s:
                                if not self.isMatch(s[s_index:], p[p_index + 2:]):
                                    s_index = s_index + 1
                                else:
                                    return True
                        # 第二种： .*a形式
                        # 下一个字符是a则进入递归
                        # 否则直接s_index + 1
                        else:
                            while s_index < len_s:
                                if p[p_index + 2] != s[s_index]:
                                    s_index = s_index + 1
                                elif not self.isMatch(s[s_index:], p[p_index + 2:]):
                                    s_index = s_index + 1
                                else:
                                    return True
                        p_index = p_index + 2
                # 任意不重复
                else:
                    p_index = p_index + 1
                    s_index = s_index + 1
            # 等于字母a-z时
            else:
                # 不任意重复
                if p_index + 1 < len_p and p[p_index + 1] == '*':
                    # 符合以下三种情况
                    # 1.*后无字符
                    # 2.*后字符满足"与*前不同且在末位"
                    # 3.*后面字符满足"与*前不同且后面不是*"
                    # 直接前进到不能前进
                    if \
                            p_index + 2 == len_p or \
                            (p[p_index + 2] != p[p_index] and p[p_index + 2] != '.'
                             and (p_index + 3 == len_p or p[p_index + 3] != '*')):
                        while s_index < len_s and p[p_index] == s[s_index]:
                            s_index = s_index + 1
                        p_index = p_index + 2
                    # 符合以下两种情况
                    # 1.后面接相同字符
                    # 2.或者后面接循环匹配符（比如b*）
                    # 递归
                    else:
                        while s_index < len_s and p[p_index] == s[s_index]:
                            # 从*消耗0字符开始递归
                            # 第二次*消耗s一个字符
                            if not self.isMatch(s[s_index:], p[p_index + 2:]):
                                s_index = s_index + 1
                            else:
                                return True
                        p_index = p_index + 2
                # 不任意不重复
                else:
                    if p[p_index] == s[s_index]:
                        p_index = p_index + 1
                        s_index = s_index + 1
                    else:
                        return False

        # 判断两种情况
        # 1.两者刚好遍历完毕
        # s遍历完毕，p只剩下循环符
        if s_index == len_s and p_index == len_p:
            return True
        elif s_index == len_s and p_index < len_p:
            return self.loopOnly(p[p_index:])
        else:
            return False

    # 判断剩下的p是不是只有循环符

    def loopOnly(self,s):
        if s == '':
            return True
        elif len(s) >= 2 and s[1] == '*':
            return self.loopOnly(s[2:])
        else:
            return False

    # 距离保护函数
    # 返回两个循环匹配符之间的距离

    # def L_FromLoop(self,s:str) -> int:
    #     fromloop = s.find('*')
    #     if fromloop == -1:
    #         return len(s)
    #     else:
    #         return fromloop - 1




# 测试集
A = Solution()
s = "bbbaccbbbaababbac"
p = ".b*b*.*...*.*c*."
print(A.isMatch(s, p))
