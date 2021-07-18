from typing import Counter


def check(mid):
    countDays = 1
    tmp = 0
    for num in [1,2,3,4,5,6,7,8,9,10]:
        tmp += num
        if tmp > mid:
            countDays+=1
            tmp = num
        print(tmp)
        print("x",end=" ")
        print(countDays)


if __name__ == '__main__':
    check(6)
    