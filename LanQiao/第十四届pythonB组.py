import math


def A():
    def judge(s):
        t = "2023"
        idx = 0
        for ss in s:
            if ss == t[idx]:
                idx += 1
            if idx == 4:
                return False
        return True
    ans = 0
    for num in range(12345678,98765433):
        s = str(num)
        if judge(s):
            ans += 1
    print(ans)
def B():
    result = [0 for r in range(4047)]

    for i in range(1, 2024):
        for j in range(i + 1, 2024):
            result[i + j] += i
    print(max(result))
    result=[r if r<=2023 else 0 for r in range(4047)]

    for i in range(3,4047):
        for j in range(1,math.ceil(i/2)):
            if i-j <= 2023:
                result[i] += j
            elif j == i // 2:
                result[i] += j//2

    print(max(result)) # 682425
def C():
    ans = 0
    s = input()
    for idx in range(1,len(s)):
        if ord(s[idx])-ord(s[idx-1]) >= 2:
            ans += (ord(s[idx]) - ord("a") + 1)
    print(ans)

def E():
    n = int(input())
    a = input()
    b = input()
    def add(ss,idx):
        ss = list(ss)
        a = int(ss[idx])
        if a < 9:
            ss[idx] = str(a+1)
        else:
            while idx >= 0:
                ss[idx] = "0"
                idx -= 1
                return add(ss,idx)
        return "".join(ss)

    def sub(ss,idx):
        ss = list(ss)
        a = int(ss[idx])
        if idx>=0 and a > 0:
            ss[idx] = str(a-1)
        else:
            while idx >= 0:
                ss[idx] = "9"
                idx -= 1
                return sub(ss,idx)
        return "".join(ss)
    ans = 0
    for i in range(n-1,-1,-1):
        if a[i] == b[i]:
            continue
        aa = int(a[i])
        bb = int(b[i])
        if aa <= bb:
            x = bb - aa
        else:
            x = 10 + bb - aa
        y = 10-x
        if x <= y :
            while x > 0:
                a = add(a,i)
                x -= 1
                ans += 1
        else:
            while y > 0:
                a = sub(a,i)
                y -= 1
                ans += 1
    # print(a,b)
    print(ans)



    # print(add("97993",3))
    # print(add("99909",2))
    # print(sub("00000",4))
    # print(sub("99999",4))
    # print(sub("00000",3))
def J():
    n = int(input())

    arr = ["","2 1","2 1 1","3 2 1","2 3 2 1","3 2 1 1","4 3 2 1","2 4 3 2 1","3 4 3 2 1","4 3 2 1 1","5 4 3 2 1"]
    if n <= 10: return arr[n]
    m = 1
    while (m+1)*m <= 2*n:
        m += 1
    r = n - (m-1)*m // 2
    # print(m,r)
    if r > 0:
        print(r+1,end=" ")
    for i in range(m,0,-1):
        print(i,end=" ")
# A()
B()
# C()
# E()
# while True:
#     J()