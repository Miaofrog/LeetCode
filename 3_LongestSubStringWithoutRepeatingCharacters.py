class Solution:
    #-----思路：滑动窗口-----#
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = -1    #str[left...right]为滑动窗口，初始里边没有任何元素
        maxSubStringLength = 0
        freq = [0] * 256    #所有字符的词频为0
        while left < len(s):
            if right + 1 < len(s) and freq[ord(s[right + 1 ])] == 0:
                right += 1
                freq[ord(s[right])] += 1    #不重复则加入滑动窗口,修改词频
            else:  #right已经到头 || freq[s[right+1]] == 1
                freq[ord(s[left])] -= 1      #重复就减少滑动窗口左边，减少之前要去除频率
                left += 1

            maxSubStringLength = max(maxSubStringLength, right - left + 1)
        return maxSubStringLength

if __name__ == "__main__":
    string1 = "abcabcbb"
    string2 = "bbbbb"
    string3 = "pwwkew"

    solu = Solution()
    print(solu.lengthOfLongestSubstring(string1))
    print(solu.lengthOfLongestSubstring(string2))
    print(solu.lengthOfLongestSubstring(string3))