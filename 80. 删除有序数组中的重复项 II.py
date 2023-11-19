class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        l_idx, r_idx = 1, 1
        cur_num = nums[0]
        cur_count = 1
        while r_idx < len(nums):
            if nums[r_idx] == cur_num:
                if cur_count < 2:
                    nums[l_idx] = cur_num
                    l_idx += 1
                cur_count += 1
            else:
                cur_num = nums[r_idx]
                cur_count = 1
                nums[l_idx] = cur_num
                l_idx += 1
            r_idx += 1
        # print(l_idx,r_idx,nums[l_idx-1],cur_num)
        return l_idx
    def removeDuplicates(self, nums):
        dic ={}
        idx = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            elif dic[num] < 2:
                dic[num] = dic[num] + 1
            else:
                continue
            nums[idx] = num
            idx += 1
        return idx

