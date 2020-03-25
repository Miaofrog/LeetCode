from typing import List

class Solution:
    #时间复杂度：O(n)
    #空间复杂度：O(n)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeronums = []
        for i in range(0, len(nums), 1):
            if nums[i] != 0:
                nonZeronums.append(nums[i])   #所有非零元素

        for i in range(0, len(nonZeronums), 1):
            nums[i] = nonZeronums[i]   #将所有非零元素放到nums前部分里

        for i in range(len(nonZeronums), len(nums), 1):
            nums[i] = 0  #nums后部分置为0


    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0    #arr[0...k)中保存非零元素
        for i in range(0, len(nums), 1):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums), 1):
            nums[i] = 0  #将arr[k...n)置为0



    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    # 最后无需将arr[k...n)置为0，交换元素过程中自然变成了0
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0  # arr[0...k)中保存非零元素，arr[k...i)保存0元素
        for i in range(0, len(nums), 1):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]  #交换非零元素和零元素
                k += 1


    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    # 最后无需将arr[k...n)置为0，交换元素过程中自然变成了0
    #对于特殊情况：如果全为非零元素，则每次都要跟自己swap，取消这种操作
    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0  # arr[0...k)中保存非零元素，arr[k...i)保存0元素
        for i in range(0, len(nums), 1):
            if nums[i] != 0:
                if k != i:
                    nums[k], nums[i] = nums[i], nums[k]  #交换非零元素和零元素
                    k += 1
                else: #k == i 自己不跟自己交换
                    k += 1




if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]

    sol = Solution()
    sol.moveZeroes3(arr)
    print(arr)


