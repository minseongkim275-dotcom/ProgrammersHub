class Solution(object):
    def twoSum(self, nums, target):
        right = len(nums)-1
        while right>0:
            left = 0
            while left < right:  
                if nums[left] + nums[right] == target:
                    return [left, right]
                left +=1
            right -= 1
        return 

"""
최악의 경우 시간 복잡도가 O(n^2)이 될 수 있기 때문에 더 나은 방법을 찾아본다.
"""

class Solution(object):
    def twoSum(self, nums: List[int]. target: int):
        seen = {}

        for k,v in enumerate(nums):
            need = target - v
            if need in seen:
                return [seen[need],k]
            seen[v] = k

        return seen

"""
twoSum의 경우 더했을 때 target이 되는 값을 찾는 것이 목적이기 때문에 배열을 돌며 찾는 값을 저장하고 딕셔너리로 바로 찾을 수 있돌고하는 것이 포인트이다.

"""
