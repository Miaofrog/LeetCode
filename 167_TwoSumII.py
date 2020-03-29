from typing import List


class Solution:

    #-----思路1：最暴力解法，双重循环遍历-----#
    #时间复杂度：O(n^2)
    #空间复杂度：O(1)
    # 提交会超时
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers), 1):
            for j in range(i + 1, len(numbers), 1):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]  #返回索引从1开始
        raise ValueError("找不到两个数的和为%d"%target)


    # -----思路2：数组有序，可以使用二分查找-----#
    # 时间复杂度：O(nlogn)
    # 空间复杂度：O(1)
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)-1, 1):
            target1 = target - numbers[i]   #转换查找元素
            #在nums[i+1...n-1]内二分查找target1
            left = i+1
            right = len(numbers) - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if numbers[mid] == target1:
                    return [i+1, mid+1]
                elif target1 < numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        raise ValueError("找不到两个数的和为%d"%target)

    # -----思路3：对撞指针----#
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:  #left=right只有一个元素，要求不同元素之和
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:  #numbers[left] + numbers[right] < target
                left += 1

        raise ValueError("找不到两个数的和为%d"%target)


if __name__ == "__main__":
    arr = [2, 7, 11, 15]

    sol = Solution()
    print(sol.twoSum3(arr, 9))
