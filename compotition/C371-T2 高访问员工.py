class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def judge(t1,t2,t3):
            h1,m1 = int(t1[:2]),int(t1[2:])
            h2,m2 = int(t2[:2]),int(t2[2:])
            h3,m3 = int(t3[:2]),int(t3[2:])
            return ((h3 - h1) * 60 + m3 - m1) < 60

        dic = {}
        for access_time in access_times:
            if access_time[0] not in dic:
                dic[access_time[0]] = [access_time[1]]
            else:
                dic[access_time[0]].append(access_time[1])
        ans = []
        for name in dic:
            if len(dic[name]) < 3:
                continue
            dic[name] = sorted(dic[name],key=lambda x:int(x))
            for i in range(len(dic[name])-2):
                if judge(dic[name][i],dic[name][i+1],dic[name][i+2]):
                    ans.append(name)
                    break

        # print(dic)
        return ans