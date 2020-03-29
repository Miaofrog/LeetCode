#给你一个数组 nums 和一个值 val，移除所有数值等于 val 的元素，并返回移除后数组的新长度。
from typing import List

#问题1：如何定义删除？是从数组中移除还是放到数组末尾。
#问题2：移除后数组是否需要改变？还是仅仅只需要返回新长度即可？
#问题3：移除后剩余元素是否需要保持原有的相对顺序？

class Solution:

    #思路1：只返回正确的新长度，但对原数组没有任何改变，实质上没有移除，不建议使用，提交通不过
    # 时间复杂度O(n)
    # 空间复杂度O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(0, len(nums), 1):
            if nums[i] == val:
                count += 1    #记录数组中等于val的个数

        return len(nums) - count  #返回剩余元素个数，但并没有对数组做任何操作



    #思路2：使用辅助空间保存非val元素，再赋值回原数组，保持了原先的排列顺序
    # 时间复杂度O(n)
    # 空间复杂度O(n)
    def removeElement1(self, nums: List[int], val: int) -> int:
        newNums = []
        for i in range(0, len(nums), 1):
            if nums[i] != val:
                newNums.append(nums[i])

        for i in range(0, len(newNums), 1):
            nums[i] = newNums[i]

        return len(newNums)


    # 思路3：原地操作，返回正确的新长度，并将等于val的元素放到元素末尾，新长度的数组是原来数组不等于val的排列，但是没有保持排列顺序
    # 时间复杂度O(n)
    #空间复杂度O(1)
    def removeElement2(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0               # nums[0...left)存放不等于val的元素,初始一个元素都没有
        right = len(nums) - 1  # nums[right+1...n-1]存放等于val的元素,初始一个元素都没有
        while left <= right:   #要考虑left==right的情况
            if nums[left] == val:
                count += 1  # 记录数组中等于val的个数
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return len(nums) - count  # 返回剩余元素个数，但并没有对数组做任何操作



    # 思路4：原地操作并保持原先的排列顺序
    # 时间复杂度O(n)
    # 空间复杂度O(n)