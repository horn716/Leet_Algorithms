# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        var=1
        L1=[]
        L2=[]
        while var==1:
            L1.insert(0,str(l1.val))
            if l1.next==None:
                break
            else:
                l1=l1.next
        L1num=int(''.join(L1))
        while var==1:
            L2.insert(0,str(l2.val))
            if l2.next==None:
                break
            else:
                l2=l2.next
        L2num=int(''.join(L2))
        sum=str(L1num+L2num)
        ltemp=ListNode(int(sum[0]))
        if len(sum)>1:
            lOut=ListNode(100)
            for i in range(1,len(sum)):
                lOut=ListNode(int(sum[i]))
                lOut.next=ltemp
                ltemp=lOut
            return lOut
        else:
            return ltemp


def main():
    A=Solution()
    l1=ListNode(2)
    l2=ListNode(4)
    l3=ListNode(3)
    l1.next=l2
    l2.next=l3
    l4=ListNode(5)
    l5=ListNode(6)
    l6=ListNode(4)
    l4.next=l5
    l5.next=l6
    l7=ListNode(0)
    l8=ListNode(0)
    lOut=A.addTwoNumbers(l7,l8)
    var=1
    while var == 1:
        print(lOut.val)
        if lOut.next == None:
            break
        else:
            lOut = lOut.next

main()