class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1

nums = [1,1,2,2]
sol = Solution()
k = sol.removeDuplicates(nums)
print("Unique Count =" , k)
print("Array after removing Duplicates:" , nums[:k])

        