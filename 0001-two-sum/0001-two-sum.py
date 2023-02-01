class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}

        for i in range(len(nums)):
            if target - nums[i] in number_to_index:
                return [number_to_index[target - nums[i]], i]
            number_to_index[nums[i]] = i

        return []

            