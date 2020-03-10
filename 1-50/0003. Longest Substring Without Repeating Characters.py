class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        if s=="":
            return 0
        elif len(s)==1:
            return 1
        else:
            length=0
            subStart=subEnd=0
            dict[s[0]]=1
            while(subEnd<len(s)-1):
                subEnd+=1
                if s[subEnd] in dict:
                    if dict[s[subEnd]]==1:
                        #计算长度，判断是否是最大长度，如果是则替换length
                        if(subEnd-subStart)>length:
                            length=subEnd-subStart
                        #找到重复字符位置作为subStart-1，在其之前的dict全部清零
                        for i in range(subStart,subEnd):
                            if(s[i]==s[subEnd]):
                                subStart=i+1
                                break
                            else:
                                dict[s[i]]=0
                    else:
                        dict[s[subEnd]]=1
                else:
                    dict[s[subEnd]]=1
            if (subEnd - subStart+1) > length:
                length = subEnd - subStart+1
            return length


def main():
    A=Solution()
    print(A.lengthOfLongestSubstring('pwwkew'))


main()