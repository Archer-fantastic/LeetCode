from typing import List


class Solution:
    # 20. 有效的括号
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for ss in s:
            if ss in ['(', '[', '{']:
                stack.append(ss)
            else:
                if len(stack) > 0 and stack[-1] == dic[ss]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    "3[a]2[bc]"
    # 394. 字符串解码
    def decodeString(self, s: str) -> str:
        stk = []
        for ss in s:
            # 不是"]"，照单全收，进栈
            if ss!="]":
                stk.append(ss)
            else:
                # 遇到"]",把"[]"裹起来的单词取出，记为word
                word = ""
                while stk[-1]!="[":
                    word = stk.pop() + word
                # 弹出"["
                stk.pop()
                # 因为会有大于10的次数，所以再写一个while，得到次数，如100
                cnt = 0
                t = 1
                while len(stk) > 0 and ord("0") <= ord(stk[-1]) <=ord("9"):
                    cnt += int(stk.pop()) * t
                    t *= 10
                # 得到重复的字符串后，继续压入栈
                _s = cnt * word
                stk.extend(list(_s))
                # for _ss in _s:
                #     stk.append(_ss)

        return "".join(stk)
    # 739. 每日温度
    # 输入: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # 输出: [1, 1, 4, 2, 1, 1, 0, 0]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = temperatures[::-1]
        stk = []
        ans = []
        for idx,t in enumerate(temperatures):
            while len(stk)>0 and temperatures[stk[-1]] <= t:
                stk.pop()
            if len(stk) == 0:
                ans.append(0)
            else:
                ans.append(idx - stk[-1])
            stk.append(idx)
        return ans[::-1]
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = []
        for idx,t in enumerate(temperatures):
            while len(stk)>0 and temperatures[stk[-1]] <= t:
                stk.pop()
            if len(stk) == 0:
                ans.append(0)
            else:
                ans.append(idx - stk[-1])
            stk.append(idx)
        return ans

def fun():
    t = int(input())

    l = []
    for i in range(t):
      tt = int(input())
      l.append(tt)

    for i in range(t):
      a = 1
      b = 1
      for j in range(l[i]-2):
        c = (a + b) % (1000000000 + 7)
        a = b
        b = c
      print(b)



s = Solution()
#
# print(s.decodeString("3[a]2[bc]"))
# print(s.decodeString(s = "3[a2[c]]"))
# print(s.decodeString("2[abc]3[cd]ef"))
# print(s.decodeString("abc3[cd]xyz"))
# print(s.decodeString("abc10[cd]xyz"))
# print(s.decodeString("100[leetcode]"))
#
# print(s.dailyTemperatures(temperatures = [73, 74, 75, 71, 69, 72, 76, 73]))
# print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

fun()