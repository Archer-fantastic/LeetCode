class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def combination(candidates,target,res_list):
            if target < 0:
                return
            if target == 0:
                res.append(res_list)
            for i,c in enumerate(candidates):
                # 为了避免重复 (例如candiactes=[2,3,6,7],target=7，输出[[2,2,3],[3,2,2][7]])
                # 传到的下一个candicate为candicates[i:]
                combination(candidates[i:],target-c,res_list+[c])

        combination(candidates,target,[])
        return res
