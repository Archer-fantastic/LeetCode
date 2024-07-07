class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            j = 1
            c = 0
            while i + j < n and (nums[i + j] + nums[i + j - 1]) % 2 != 0:
                j += 1
                c += 1
            # print("j:",j,"c:",c)
            res += (c * (c + 1) // 2)
            if c == 0:
                i += 1
            else:
                i += j

        # for i in range(n):
        #     for j in range(1,n):
        #         if i+j<n and (nums[i+j] + nums[i+j-1]) % 2 !=0:
        #             res += 1
        #         else:
        #             break
        return res + n

