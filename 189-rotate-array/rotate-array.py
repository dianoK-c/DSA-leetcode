class Solution(object):
    def rotate(self, nums, k):
       n = len(nums)
       if n == 0 or k==0:
        return nums
       k = k % n 
       self.reverse(nums, 0, n - 1)   # reverse whole array
       self.reverse(nums, 0, k - 1)   # reverse first k elements
       self.reverse(nums, k, n - 1)   # reverse remaining elements

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1