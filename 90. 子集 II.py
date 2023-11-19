class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_list = []
        n = len(nums)
        for i in range(2**n):
            num_list.append(bin(i)[2:].zfill(n))
        ans = []
        for num in num_list:
            tmp = []
            for idx in range(n):
                if num[idx] == "1":
                    tmp.append(nums[idx])
            tmp = sorted(tmp)
            if tmp not in ans:
                ans.append(tmp)
        return ans