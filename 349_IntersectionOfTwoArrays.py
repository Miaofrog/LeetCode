#给定两个数组，编写一个函数来计算它们的公共元素。
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #将nums1中元素全部放入set中
        set1 = set(nums1)  #set1中存储nums1中无重复元素
        set2 = set(nums2)  # set2中存储nums2中无重复元素

        #在set中查找nums2中元素
        result = []
        for num in set1 & set2:  #直接求两个set的交集
            result.append(num)

        return result

if __name__ == "__main__":
    solu = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solu.intersection(nums1, nums2))

