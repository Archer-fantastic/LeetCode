import os
import sys

# 请在此输入您的代码
def funA():
  s = input()
  cnt = s.count("?")

  dic = {i:-1 for i in range(cnt)}
  idx = 0

  for i in range(len(s)):
    if s[i] == "?":
      dic[idx] = i
      idx += 1

  arr = []
  for i in range(2**cnt):
    arr.append(bin(i)[2:].zfill(cnt))

  def cal(s):
    ans = 0
    idx = 0
    while idx < len(s):
      if idx+1 < len(s) and s[idx] == s[idx+1]:
        idx += 2
        ans += 1
      else:
        idx += 1
    return ans

  res = 0
  for a in arr:
    s = list(s)
    idx = 0
    for _ in range(cnt):
      if a[idx] == "0":
        s[dic[idx]] = "0"
      else:
        s[dic[idx]] = "1"
      idx += 1
    s = "".join(s)
    res = max(res,cal(s))
  print(res)

def B():
  n, m = list(map(int, input().split(" ")))


  dic1 = {i: 0 for i in range(1, n + 1)}
  dic2 = {i: 0 for i in range(1, n + 1)}

  for _ in range(m):
    a, b, c, d = list(map(int, input().split(" ")))
    for i in range(a, c + 1):
      dic1[i] += 1
    for j in range(b, d + 1):
      dic2[j] += 1

  for i in range(1,n+1):
    for j in range(1,n+1):
      print((dic1[i] + dic2[j]) % 2, end="")
    print()
B()
