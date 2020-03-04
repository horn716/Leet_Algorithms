# ZigZag直接横向读取的解法
# z化后的每一行的新坐标
# 与row和当前行k有一定关系
# 利用这个关系避免使用len*len的表格
# 距离：指输入字符串中两个字符隔了几个位置
# 比如s[0]和s[3]的距离就是3

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        # 新建一个空数组用来存放答案
        s_Output = []

        if numRows == 1:
            return s
        # 当前行
        k = 0
        # 下一个将要被append的字符的下标
        i = 0

        # 分成三段讨论，Z分为竖线和折线两部分
        # 对于竖线部分，同行的距离永远是
        # 前坐标+2（z行数-1）
        # 所以首行/尾行可以直接使用这个公式
        # 但中间行两条竖线间还有折线
        # 虽然同行竖线字符间距离相等，但折线上的字符
        # 会随着行数增加而左移，所以需要分开来讨论

        # 首行
        # 第二个开始坐标等于
        # 前坐标+2（行数+1-当前行数）
        while i < len_s:
            s_Output.append(s[i])
            i = i + 2 * (numRows - 1)

        # 中间行
        # 对每一行的处理
        for k in range(1,numRows - 1):
            # 初始化i
            i = k
            # 判断下一个元素是不是折线元素
            # 如果是就是true
            is_z = True
            while i < len_s:
                s_Output.append(s[i])
                if is_z:
                    i = i + 2 * (numRows - 1 - k)
                    is_z = False
                else:
                    i = i + 2 * k
                    is_z = True

        # 尾行
        # 与首行相等
        k = numRows - 1
        i = k
        while i < len_s:
            s_Output.append(s[i])
            i = i + 2 * (numRows - 1)




        return ''.join(s_Output)



s01 = "A"
A = Solution()
print(A.convert(s01,1))
