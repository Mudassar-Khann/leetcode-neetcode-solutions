class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}

        for i, j in enumerate(nums):
            check = a.get(target - j)
            if check is not None:
              return [check, i]
            a[j] = i
            

        return []
        