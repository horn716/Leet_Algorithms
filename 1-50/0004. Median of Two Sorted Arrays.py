from typing import List
# 思路：设置一个中位数计步器，模拟归并，计步器为0的时候触发返回中位数的动作
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        Len = len(nums1)+len(nums2)
        index01 = 0
        index02 = 0
        median = 0
        # 总长度是奇数的情况下 中位数计步器index_threshold代表归并后数组的第index_threshold个数字就是中位数
        if Len%2 == 1:
             index_threshold = (Len // 2) + 1  # 奇数时的中位数计步器
             while index01<len(nums1) and index02<len(nums2):  # 两方下标都没有溢出的情况下的对比
                if nums1[index01] < nums2[index02]:
                    median = nums1[index01]
                    index01 += 1
                    index_threshold -= 1
                else:
                    median = nums2[index02]
                    index02 += 1
                    index_threshold -= 1
                if index_threshold == 0:
                    return median
             # 溢出的是nums1
             if index01 == len(nums1):
                 median = nums2[index02 + (index_threshold - 1)]
                 return median
             # 溢出的是nums2
             else:
                 median = nums1[index01 + (index_threshold - 1)]
                 return median

        # 总长度是偶数的情况下 中位数计步器index_threshold代表归并后数组的第index_threshold个数字和下一个数字的平均数就是中位数
        else:
             index_threshold = Len // 2  # 奇偶数时的中位数计步器
             while index01<len(nums1) and index02<len(nums2):  # 两方下标都没有溢出的情况下的对比
                if nums1[index01] < nums2[index02]:
                    median = nums1[index01]
                    index01 += 1
                    index_threshold -= 1
                else:
                    median = nums2[index02]
                    index02 += 1
                    index_threshold -= 1
                # 在两方下标都没有溢出（或者刚好到最后一位）的情况下计步器到0
                if index_threshold == 0:
                    # 如果两边都没有到最后一位，按照通常比较出下一个数，取平均值
                    if index01<len(nums1) and index02<len(nums2):
                        if nums1[index01] < nums2[index02]:
                            median = (median + nums1[index01]) / 2
                            return median
                        else:
                            median = (median + nums2[index02]) / 2
                            return median
                    # 如果nums1数组用光，中位数等于现在的中位数加上nums2当前数字
                    if index01 == len(nums1):
                        median = (median + nums2[index02]) / 2
                        return  median
                    # 如果nums2数组用光，中位数等于现在的中位数加上nums1当前数字
                    if index02 == len(nums2):
                        median = (median + nums1[index01]) / 2
                        return median
             #nums1用光，计步器还没有走完的情况： 将nums2直接跳到中位数计步器走完为止，并计算当前数字和下一个数字的平均值
             if index01 == len(nums1):
                 median = (nums2[index02 + index_threshold -1] + nums2[index02 + index_threshold]) / 2
                 return median
             #nums1用光，计步器还没有走完的情况： 将nums2直接跳到中位数计步器走完为止，并计算当前数字和下一个数字的平均值
             if index02 == len(nums2):
                 median = (nums1[index01 + index_threshold -1] + nums1[index01 + index_threshold]) / 2
                 return median










def main():
    input_nums1=[1,2]
    input_nums2=[1,1]
    A=Solution()
    print(A.findMedianSortedArrays(input_nums1,input_nums2))


main()




