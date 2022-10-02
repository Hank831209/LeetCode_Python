'''
Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''


class Solution(object):
    # 解法1, 拿最短的str長度去一個一個比
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = list()
        for i in strs:
            a.append(len(i))
        num = min(a)
        ans = ''
        if num == 0:  # list中有空字串
            return ans
        for i in range(1, num + 1):  # 取字數
            check = strs[0][:i]  # 取前幾個字
            for j in strs:  # 列表
                if j[:i] != check:  # 出現相異的字就回傳
                    return ans
            ans = check
        return ans

    def longestCommonPrefix_2(self, strs):
        if not strs:  # 空list的話回傳空字串
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1
    # 解法3, 拿第一個str去比, 遇到長度比它短的或是不符合的,
    # 就刪字數慢慢比
    def longestCommonPrefix_3(self, strs):
        if not strs:  # 空list的話回傳空字串
            return ""
        prefix = strs[0]
        count = len(strs)  # 確保進入迴圈
        while count != len(strs) - 1:
            count = 0
            for j in range(1, len(strs)):  # 要比對的字串index
                if len(prefix) > len(strs[j]):
                    prefix = prefix[0:len(strs[j])]
                    break
                if prefix != strs[j][0:len(prefix)]:  # 比對失敗 prefix刪一個字
                    prefix = prefix[0:len(prefix) - 1]
                    break
                if prefix == strs[j][0:len(prefix)]:
                    count = count + 1
        return prefix


# ['flower', "flow", "flight"]
# strs = ["dog", "racecar", "car"]
strs = ['flower', "flow", "flight"]
print(min(strs))
# ans = Solution()
# Ans = ans.longestCommonPrefix_3(strs)





