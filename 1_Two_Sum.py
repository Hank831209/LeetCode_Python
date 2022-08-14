# Description:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up
# to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
class Solution(object):
    # 很直觀的思路, 一個一個看但速度相對較慢(時間複雜度高, O(N^2))
    def twoSum_Solution1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

    # List的數字只會掃過一遍(時間複雜度低, O(N))
    # 利用python字典的 __contains__方法(查詢字典中是否存在該key值),
    # get方法(給定key值回傳value值)完成
    def twoSum_Solution2(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            if num_map.__contains__(target - nums[i]):
                return [num_map.get(target - nums[i]), i]
            else:
                num_map[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
ans = Solution()
Ans2 = ans.twoSum_Solution2(nums, target)
Ans1 = ans.twoSum_Solution1(nums, target)
print(Ans1)
print(Ans2)



