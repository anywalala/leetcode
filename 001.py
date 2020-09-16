class Solution:
    def twoSum(self, nums, target):
        count1 = 0
        for num1 in nums:
            count2 = count1 + 1
            for num2 in nums[count1+1: ]:
                if num1 + num2 == target:
                    return [count1, count2]
                count2 = count2 + 1
            count1 = count1 + 1

    def twoSum1(self, nums, target):
        _dict = {}
        for i, num in enumerate(nums):
            if _dict.get(target-num) != None:
                return [_dict.get(target-num), i]
            _dict[num] = i


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum1(nums, target)
    print result