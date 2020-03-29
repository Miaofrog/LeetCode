from typing import List


class Solution:

    #-----思路一：计数排序-----#
    #分别统计0,1,2的元素个数，在放回原数组中
    # 时间复杂度：O(n)
    # 空间复杂度：O(k) = O(1)  k是数组中不同元素个数
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in range(0, len(nums), 1):
            assert nums[i] >= 0 and nums[i] <= 2    #不能有其他元素
            count[nums[i]] += 1   #统计词频

        #再将0,1,2放回原数组
        index = 0
        for i in range(0, count[0], 1):
            nums[index] = 0
            index += 1

        for i in range(0, count[1], 1):
            nums[index] = 1
            index += 1

        for i in range(0, count[2], 1):
            nums[index] = 2
            index += 1




    # -----思路二：三路快排-----#
    # 只遍历原数组一遍
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1          # 保持nums[0...zero] == 0,初始化为一个元素都没有为-1
        two = len(nums)    # 保持nums[two...n-1] == 2,初始化为一个元素都没有为n
        index = 0          #遍历指针
        while index < two:    # index == two 时为2
            if nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                two -= 1
                nums[index], nums[two] = nums[two], nums[index]  #index无需做--
            else:
                assert nums[index] == 0    #其他元素则报错
                zero += 1
                nums[index], nums[zero] = nums[zero], nums[index]
                index += 1



if __name__ == "__main__":
    arr = [2,0,2,1,1,0]

    sol = Solution()
    sol.sortColors1(arr)
    print(arr)