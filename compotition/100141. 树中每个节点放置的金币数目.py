from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        def get(nodes,i):

            res = []
            stack = [i]
            while len(stack)>0:
                idx = stack.pop()
                res.append(cost[idx])
                for j in nodes[idx]:
                    stack.append(j)
            # res=res[1:]
            res = sorted(res,key=lambda x:-abs(x))
            print(i,res)
            n = len(res)
            if n < 3:
                return 1
            a,b,c = res[0],res[1],res[2]
            tmp = a * b * c
            if tmp > 0:
                return tmp
            if a<0 and b < 0 and c < 0:
                idx = 3
                while idx < n and res[idx] <= 0:
                    idx += 1
                if idx == n:
                    return 0
                return a*b*res[idx]
            elif a == 0:
                if n == 3:
                    return 0
                idx = 3
                while idx < n and res[idx] >= 0:
                    idx += 1
                if idx == n:
                    return b * c * res[3]
                else:
                    return max(b * a * res[idx],b * c * res[3])
            elif b == 0:
                if n == 3:
                    return 0
                idx = 3
                while idx < n and res[idx] >= 0:
                    idx += 1
                if idx == n:
                    return a * c * res[3]
                else:
                    return max(a * b * res[idx], a * c * res[3])
            else:
                if n == 3:
                    return 0
                idx = 3
                while idx < n and res[idx] >= 0:
                    idx += 1
                if idx == n:
                    return a * c * res[3]
                else:
                    return max(a * b * res[3], a * c * res[idx])




        n = len(cost)
        nodes = {i:[] for i in range(n)}
        for edge in edges:
            nodes[edge[0]].append(edge[1])
        print(nodes)
        # for node in nodes:
        #     nodes[node] = sorted(nodes[node],key=lambda x:-abs(cost[x]))
        # print(nodes)
        ans = []
        for i in range(n):
            res = get(nodes,i)

            ans.append(res)
        return ans
s = Solution()
# print(s.placedCoins([[0,2],[0,6],[1,4],[3,5],[7,6],[3,6],[1,8],[3,1],[9,3]],
# [63,13,-6,20,56,-14,61,25,-99,54]))
# print(s.placedCoins(edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]))
# print(s.placedCoins(edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]))
print(s.placedCoins([[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[0,20],[0,21],[0,22],[0,23],[0,24],[0,25],[0,26],[0,27],[0,28],[0,29],[0,30],[0,31],[0,32],[0,33],[0,34],[0,35],[0,36],[0,37],[0,38],[0,39],[0,40],[0,41],[0,42],[0,43],[0,44],[0,45],[0,46],[0,47],[0,48],[0,49],[0,50],[0,51],[0,52],[0,53],[0,54],[0,55],[0,56],[0,57],[0,58],[0,59],[0,60],[0,61],[0,62],[0,63],[0,64],[0,65],[0,66],[0,67],[0,68],[0,69],[0,70],[0,71],[0,72],[0,73],[0,74],[0,75],[0,76],[0,77],[0,78],[0,79],[0,80],[0,81],[0,82],[0,83],[0,84],[0,85],[0,86],[0,87],[0,88],[0,89],[0,90],[0,91],[0,92],[0,93],[0,94],[0,95],[0,96],[0,97],[0,98],[0,99]]
,[-5959,602,-6457,7055,-1462,6347,7226,-8422,-6088,2997,-7909,6433,5217,3294,-3792,7463,8538,-3811,5009,151,5659,4458,-1702,-1877,2799,9861,-9668,-1765,2181,-8128,7046,9529,6202,-8026,6464,1345,121,1922,7274,-1227,-9914,3025,1046,-9368,-7368,6205,-6342,8091,-6732,-7620,3276,5136,6871,4823,-1885,-4005,-3974,-2725,-3845,-8508,7201,-9566,-7236,-3386,4021,6793,-8759,5066,5879,-5171,1011,1242,8536,-8405,-9646,-214,2251,-9934,-8820,6206,1006,1318,-9712,7230,5608,-4601,9185,346,3056,8913,-2454,-3445,-4295,4802,-8852,-6121,-4538,-5580,-9246,-6462]))
