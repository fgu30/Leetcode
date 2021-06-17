N = 10
a = [0] * N
q = [-1] * N
head, tail = 0, -1

def main():
    global a, q, tail, head
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().rstrip().split(" ")))

    for i in range(n):
           
        if(head <= tail and i - k + 1 > q[head]): 
            head +=1
        while(head <= tail and a[q[tail]] >= a[i]): 
            tail -= 1
        tail += 1
        print("q的tail = {}位置被赋值i = {} ".format(tail,i))
        q[tail] = i
        print(head,tail,a,q)  
        if(i >= k - 1): 
            print(a[q[head]])
        print('='*100)

    # i, head, tail = 0, 0, -1
    # for i in range(n):
    #     if(head <= tail and i - k + 1 > q[head]): head +=1
    #     while(head <= tail and a[q[tail]] <= a[i]): tail -= 1
    #     tail += 1
    #     q[tail] = i
    #     if(i >= k - 1): print(a[q[head]], end=" ")
    # print()


main()


