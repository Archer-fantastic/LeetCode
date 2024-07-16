from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]],count=-1) -> List[List[str]]:
        # 题目：给定一组 [人名+邮箱名] * n，现在要进行账户合并的操作。
        # 这道题一定有树形搜索、DFS、并查集这些方法，But如果是我们自己肉眼看的话我们不会用到并查集这些算法。
        # 因此就来模拟一下这个合并过程,把自己的思路写成代码，当然代码最后很冗长，建议只看思路不看代码。
        # Step1：观察一下数据，我们主要做一个去重和合并的功能，这些邮箱名不太方便查看，于是我们可以用字典把它映射成数字
        '''
            [['David', 'David4@m.co', 'David2@m.co', 'David4@m.co']
            ['John', 'John7@m.co', 'John5@m.co', 'John3@m.co']
            ['Fern', 'Fern6@m.co', 'Fern4@m.co', 'Fern5@m.co']
            ['Celine', 'Celine0@m.co', 'Celine7@m.co', 'Celine7@m.co']
            ['Gabe', 'Gabe8@m.co', 'Gabe8@m.co', 'Gabe1@m.co']
            ['Ethan', 'Ethan1@m.co', 'Ethan6@m.co', 'Ethan6@m.co']
            ['Celine', 'Celine4@m.co', 'Celine8@m.co', 'Celine6@m.co']
            ['Celine', 'Celine0@m.co', 'Celine0@m.co', 'Celine4@m.co'] ]
        '''
        dic = {}    # 邮箱名：数字
        _dic = {}   # 数字：邮箱名
        cnt = 1     # 数字下标
        for account in accounts:
            for idx in range(1,len(account)):
                if account[idx] not in dic:
                    dic[account[idx]] = cnt
                    _dic[cnt] = account[idx]
                    account[idx] = cnt
                    cnt += 1
                else:
                    account[idx] = dic[account[idx]]
        '''
            效果如下：dic:
            David2@m.co : 2	    John7@m.co : 3	    John5@m.co : 4	    John3@m.co : 5	    Fern6@m.co : 6	
            Fern4@m.co : 7	    Fern5@m.co : 8	    Celine0@m.co : 9	Celine7@m.co : 10	Gabe8@m.co : 11	
            Gabe1@m.co : 12	    Ethan1@m.co : 13	Ethan6@m.co : 14	Celine4@m.co : 15	Celine8@m.co : 16	
            Celine6@m.co : 17
            
            accounts:
            ['David', 1, 2, 1]
            ['John', 3, 4, 5]
            ['Fern', 6, 7, 8]
            ['Celine', 9, 10, 10]
            ['Gabe', 11, 11, 12]
            ['Ethan', 13, 14, 14]
            ['Celine', 15, 16, 17]
            ['Celine', 9, 9, 15]
        '''
        '''
        Step2：接下来的事情就是检查重复，然后去重 （核心代码）
            这里采用了一个标记数组，需要考虑一下数据量，这道题的数据量最大是1000*10，可接受范围
            以这个用例为例 一共有[-1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]17个标记
            遍历David：[-1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            遍历John：[-1, 0, 0, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            遍历Fern：[-1, 0, 0, 1, 1, 1, 2, 2, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            遍历Celine：[-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, -1, -1, -1, -1, -1, -1, -1]
            遍历Gabe：[-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, -1, -1, -1, -1, -1]
            遍历Ethan：[-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, -1, -1, -1]
            遍历Celine：[-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
        '''

        # 上面很巧合地没有发生重复，接下来最后一个Celine，可以看到9已经被标记了，
        # 那就说明这个Celine和标记了9的这个人是同一个人，于是我们需要把['Celine', 9, 9, 15]与['Celine', 9, 10, 10]进行合并
        # 得到['Celine', 9, 10, 10, 9, 9, 15]，顺便给这个Celine标记一下，表示这一项没用了

        target = [-1 for _ in range(cnt+1)]
        TT = [True for _ in range(len(accounts))]
        ans = []
        for i,account in enumerate(accounts):
            T = True
            for idx in range(1, len(account)):
                if target[account[idx]] >= 0:
                    T = False
                    TT[i] = False
                    break
            if T:
                for k in range(1, len(account)):
                    target[account[k]] = i
            else:
                for j in range(1, len(account)):
                    accounts[target[account[idx]]].append(account[j])
        '''
            新的accounts：
            ['David', 1, 2, 1] True
            ['John', 3, 4, 5] True
            ['Fern', 6, 7, 8] True
            ['Celine', 9, 10, 10, 9, 9, 15] True
            ['Gabe', 11, 11, 12] True
            ['Ethan', 13, 14, 14] True
            ['Celine', 15, 16, 17] True
            ['Celine', 9, 9, 15] False
        '''
        '''
            去重：
            ['David', 1, 2] True
            ['John', 3, 4, 5] True
            ['Fern', 8, 6, 7] True
            ['Celine', 9, 10, 15] True
            ['Gabe', 11, 12] True
            ['Ethan', 13, 14] True
            ['Celine', 16, 17, 15] True
            ['Celine', 9, 15] False
        '''
        for i,account in enumerate(accounts):
            accounts[i] = [accounts[i][0]] + list(set(accounts[i][1:]))
        for i,a in enumerate(accounts):
            print(a,TT[i])
        '''
            接下来把accounts的1-17翻译回去原来的邮箱名称，再根据后面的标记判断是否加入ans即可
            但是这里出现了一个问题：
            ['Celine', 9, 10, 15] True 和 ['Celine', 16, 17, 15] True 
            事实上是有重合的，但是我们一遍遍历其实是解决不了问题的。思考一下怎么处理这个问题
            这里的ans长这样：
            ['David', 'David2@m.co', 'David4@m.co']
            ['John', 'John3@m.co', 'John5@m.co', 'John7@m.co']
            ['Fern', 'Fern4@m.co', 'Fern5@m.co', 'Fern6@m.co']
            ['Celine', 'Celine0@m.co', 'Celine4@m.co', 'Celine7@m.co']
            ['Gabe', 'Gabe1@m.co', 'Gabe8@m.co']
            ['Ethan', 'Ethan1@m.co', 'Ethan6@m.co']
            ['Celine', 'Celine4@m.co', 'Celine6@m.co', 'Celine8@m.co']
            
            所以解决思路就是，再执行一次self.accountsMerge(ans)方法，再给一个递归终止条件
            我们给函数传入一个参数值为进入函数时的数组长度，self.accountsMerge(ans,len(ans))
            当后续所得到的ans与这个长度一致，就说明没有发生合并，可以返回
            
            例如这个极端的测试用例，最后全部汇合成一个
            print(s.accountsMerge([["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]))
            
            ['Hanzo', 1, 2, 3] True
            ['Hanzo', 9, 3, 4] True
            ['Hanzo', 1, 5, 6] True
            ['Hanzo', 2, 3] False
            ['Hanzo', 8, 9, 7] True
            ['Hanzo', 1, 6] False
            ['Hanzo', 9, 7] False
            ['Hanzo', 9, 4] False
            **************************************************
            ['Hanzo', 1, 2, 3, 4, 5, 6, 7] True
            ['Hanzo', 3, 4, 5] False
            ['Hanzo', 1, 6, 7] False
            ['Hanzo', 8, 9, 5] True
            **************************************************
            ['Hanzo', 1, 2, 3, 4, 5, 6, 7, 8, 9] True
            ['Hanzo', 8, 9, 7] False
            **************************************************
            ['Hanzo', 1, 2, 3, 4, 5, 6, 7, 8, 9] True
        '''
        for i,account in enumerate(accounts):
            if TT[i]:
                for j in range(1,len(accounts[i])):
                    account[j] = _dic[account[j]]
                ans.append([account[0]] + sorted(set(account[1:])))

        # print(TT)
        # for a in ans:
        #     print(a)
        if count == len(ans):
            return ans
        else:
            print("*"*50)
            return self.accountsMerge(ans,len(ans))

s = Solution()
# print(s.accountsMerge(accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
# print(s.accountsMerge(accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
#
# print(s.accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]))
# print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))

# print(s.accountsMerge([["David","David4@m.co","David2@m.co","David4@m.co"],["John","John7@m.co","John5@m.co","John3@m.co"],["Fern","Fern6@m.co","Fern4@m.co","Fern5@m.co"],["Celine","Celine0@m.co","Celine7@m.co","Celine7@m.co"],["Gabe","Gabe8@m.co","Gabe8@m.co","Gabe1@m.co"],["Ethan","Ethan1@m.co","Ethan6@m.co","Ethan6@m.co"],["Celine","Celine4@m.co","Celine8@m.co","Celine6@m.co"],["Celine","Celine0@m.co","Celine0@m.co","Celine4@m.co"]]))

print(s.accountsMerge([["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]))