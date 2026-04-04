class Solution(object):
    
    @staticmethod
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
                
if __name__ == "__main__":
    t = [1,2,4,6]
    x = 5
    print(Solution.twoSum(1,t, x))