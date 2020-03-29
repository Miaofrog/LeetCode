from typing import List


class Solution:


    #-----思路1：暴力解法：先找到所有子数组，然后计算sum，判断sum>=s，找到最短子数组的长度
    #时间复杂度：O(n^3)
    #空间复杂度：O(1)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        pass


    # -----思路1：优化暴力解法：先找到所有子数组，然后快速计算sum，判断sum>=s，找到最短子数组的长度
    # 时间复杂度：O(n^2)
    # 空间复杂度：O(1)
    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        pass



    # -----思路3：双索引技术：滑动窗口解法
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def minSubArrayLen3(self, s: int, nums: List[int]) -> int:
        left = 0
        right = -1    #nums[left...right]为滑动窗口，初始里边没有任何元素
        sum = 0
        minSubarrayLength = len(nums) + 1   #初始最大，最小子数组长度为nums的长度，多一个就可以
        while left < len(nums):
            if right + 1 < len(nums) and sum < s:
                right += 1
                sum += nums[right]   #更新sum,一直到找到一个sum>=s的滑动窗口
            else: #sum >= s
                sum -= nums[left]   #减少滑动窗口的长度，保持sum>=s
                left += 1

            if sum >= s:
                minSubarrayLength = min(minSubarrayLength, right - left + 1)
                #这一步不能放入else里，因为if里边sum增加之后可能大于等于s

        if minSubarrayLength == len(nums) + 1:
            return 0   #minSubarrayLength未更新,无解情况
        return minSubarrayLength   #minSubarrayLength更新了则返回


if __name__ == "__main__":
    arr = [2,3,1,2,4,3]

    sol = Solution()
    print(sol.minSubArrayLen3(7, arr))