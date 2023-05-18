class Solution(object):

    def two_sum(self, nums, target):
        if nums is None or target is None:
            raise TypeError('nums or target cannot be None')
        if not nums:
            raise ValueError('nums cannot be empty')
        cache = {}
        for index, num in enumerate(nums):
            cache_target = target - num
            if num in cache:
                return [cache[num], index]
            else:
                cache[cache_target] = index
        return None

solution = Solution()
target = 5
nums = [1, 2, 3]

print(solution.two_sum(nums, target))