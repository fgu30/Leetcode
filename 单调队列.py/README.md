- 滑动窗口记录的是当前的 index

```
import collections

N = 1000010
a = [0] * N

deq = collections.deque([])


def main():
    global a, deq
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().rstrip().split(" ")))

    for i in range(n):

        if deq and deq[0] < i - k  + 1:
            deq.popleft()
        while deq and a[deq[-1]] >= a[i]:
            deq.pop()
        deq.append(i)

        if i >= k - 1: print(a[deq[0]],end = " ")
    print()

    #deq clear

    deq.clear()

    for i in range(n):


        if deq and deq[0] < i - k  + 1:
            deq.popleft()
        while deq and a[deq[-1]] <= a[i]:
            deq.pop()
        deq.append(i)

        if i >= k - 1: print(a[deq[0]],end = " ")
    print()


main()
```
