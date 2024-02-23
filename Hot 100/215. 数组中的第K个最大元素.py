import heapq
from typing import List


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        # 先将前k个元素入堆
        heap = [nums[i] for i in range(0, k)]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)  # 弹出堆顶元素
                heapq.heappush(heap, nums[i])  # nums[i] 入堆
        return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        return nums[-k]
s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))