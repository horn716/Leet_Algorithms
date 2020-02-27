from typing import List

nums=[2,7,11,15]
def main(nums:List[int],target:int) -> List[int]:
    count=len(nums)
    for i in range(0,count):
        for j in range(i+1,count):
            if(nums[i]+nums[j]==target):
                return [i,j]
    return None

print(main(nums,9))
