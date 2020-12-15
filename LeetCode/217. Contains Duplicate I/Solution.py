class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = dict()
        for i in nums:
            if i in map:
                return True
            else:
                map[i] = None
        return False
