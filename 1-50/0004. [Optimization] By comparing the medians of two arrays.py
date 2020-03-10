class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        #保证arr1比arr2短
        if len1 > len2:
            return self.findMedianSortedArrays(nums2,nums1)
        #保证两个不是同时是空的
        if len2 == 0:
            return ValueError
        if len1 == 0:
            median_index = int(len2 / 2)
            if(len2 % 2 == 0):
                return (nums2[(median_index) - 1] + nums2[median_index]) / 2
            else:
                median = nums2[median_index]
                return median

        #二分搜索的下标
        low = 0
        high = len1

        #左边加起来的总量（odd：一半多一个  even：一半）
        half_length = int((len1 + len2 + 1) / 2)

        #二分搜索
        while low <= high:
            #X和Y的左半部分的数量,用来表示坐标
            partitionX = int((low + high) / 2)
            partitionY = int(half_length - partitionX)

            #PartitionX = 0 代表arr1 全部在右边(右边可能还有arr2的一部分)
            #PartitionX = len1 代表arr1 全部在左边（左边只有arr1）
            #PartitionY也是同理，这四种情况，虽然有作为下标[PartitionX+1]等会出错
            #但是此时由于绝对是正确答案，所以不需要做值的对比探讨，归类到perfect情况中

            #arr1的分割线需要往左移一部分
            if partitionX > 0 and nums1[partitionX - 1] > nums2[partitionY]:
                high = partitionX - 1
            #arr2的分割线需要往右移一部分
            elif  partitionX < len1 and nums2[partitionY - 1] > nums1[partitionX]:
                low = partitionX + 1

            #完美的情况
            else:
                #计算左边部分的最大值
                #由于要计算partition - 1，如果下标出现负数会出错，所以特殊情况优先处理
                #Case1: arr1全部在右边，右边可能还有arr2的一部分
                if partitionX == 0:
                    left_max = nums2[partitionY - 1]
                #Case2: arr2全部在右边，右边可能还有arr1的一部分
                elif partitionY == 0:
                    left_max = nums1[partitionX - 1]
                #Case3: 左边不是临界值
                else:
                    left_max = max(nums1[partitionX - 1],nums2[partitionY - 1])

                #计算右边部分的最小值
                #由于要计算partition，如果下标超出数组长度会出错，所以特殊情况优先处理
                #Case1: arr1全部被分在左边，左边可能还有arr2的一部分
                if partitionX == len1:
                    right_min = nums2[half_length - len1]
                #Case2: arr2全部被分在左边，左边可能还有arr1的一部分
                elif partitionY == len2:
                    right_min = nums1[half_length - len2]
                #Case3: 右边不是临界值
                else:
                    right_min = min(nums1[partitionX],nums2[partitionY])


                #得出中位数
                #Case1: odd
                if (len1 + len2) % 2 == 1:
                    median = left_max
                else:
                    median = (left_max + right_min) / 2

                return median

def main():
    arr1=[1]
    arr2=[2,3,4]
    A=Solution()
    print(A.findMedianSortedArrays(arr1,arr2))


main()