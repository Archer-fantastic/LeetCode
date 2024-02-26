import heapq
from typing import List


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def init(nums):
            def fun(nums,j,_len):
                if j >= _len:
                    return
                if 2*j+1<_len and nums[2*j+1] > nums[j]:
                    nums[2*j+1],nums[j] = nums[j],nums[2*j+1]
                if 2*j+2<_len and nums[2*j+2] > nums[j]:
                    nums[2*j+2],nums[j] = nums[j],nums[2*j+2]
                fun(nums,2*j+1,_len)
                fun(nums,2*j+2,_len)
            i = len(nums) // 2 - 1
            _len = len(nums)
            for idx in range(i,-1,-1):
                fun(nums,idx,_len)
            nums[0], nums[-1] = nums[-1], nums[0]
            # print(nums)
            return nums
        _len = len(nums)
        for i in range(k):
            nums = init(nums[:_len-i])
        return nums[-1]
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        # 先将前k个元素入堆
        heap = [nums[i] for i in range(0, k)]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)  # 弹出堆顶元素
                heapq.heappush(heap, nums[i])  # nums[i] 入堆
        return heap[0]
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # 先将前k个元素入堆
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
            print(heap)
        # 弹出堆顶元素
        return -heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        return nums[-k]
s = Solution()
print(s.findKthLargest3([3,2,3,1,2,4,5,5,6], k = 4))
print(s.findKthLargest3([3,2,1,5,6,4], k = 2))