#给定两个数组，编写一个函数来计算它们的交集。计算频次
#交集存在重复元素
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #计算nums1中元素的频次
        dict = {}   #空字典
        for num in nums1:
            if num not in dict:  #不存在该元素则添加元素
                dict[num] = 1
            else:
                dict[num] += 1

        #在dict中查找nums2中元素
        result = []
        for num in nums2:
            if num in dict:
                result.append(num)
                dict[num] -= 1
                if dict[num] == 0:   #如果这个键值为0了应该从字典中删除，否则会继续进入这个if
                    dict.pop(num)

        return result

if __name__ == "__main__":
    solu = Solution()
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solu.intersection(nums1, nums2))
