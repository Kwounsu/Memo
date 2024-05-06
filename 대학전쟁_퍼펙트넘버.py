'''
이 문제에 숫자 1이 ( )개 있다.
이 문제에 숫자 2가 ( )개 있다.
이 문제에 숫자 3이 ( )개 있다.
이 문제에 숫자 4가 ( )개 있다.
이 문제에 숫자 5가 ( )개 있다.
이 문제에 숫자 6이 ( )개 있다.
이 문제에 숫자 7이 ( )개 있다.

답: 4-3-2-2-1-1-1

아래 코드에서 N의 값을 7이 아닌 다른 값으로 바꿀 수 있다.
'''

def f(x):
    if x>N:
        for i in range(1,N+1):
            if cnt[i]!=A[i]: return
        for num in A:
            print(f"이 문제에 숫자 {num}이 ({A[num]})개 있다.")
        return 1
    for i in range(cnt[x],N+1):
        A[x]=i
        cnt[i]+=1
        if f(x+1): return 1
        cnt[i]-=1

N=7
cnt=[1]*(N+1)
A={i:0 for i in range(1,N+1)}
f(1)
