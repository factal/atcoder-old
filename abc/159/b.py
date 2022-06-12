def P(s):
  return s==s[::-1]
 
S=list(input())
N=len(S)
print('Yes' if P(S) and P(S[:N//2]) and P(S[N//2+1:]) else 'No')