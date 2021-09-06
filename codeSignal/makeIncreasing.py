'''
Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

Example

For numbers = [1, 5, 10, 20], the output should be makeIncreasing(numbers) = true.

The initial array is already strictly increasing, so no actions are required.

For numbers = [1, 3, 900, 10], the output should be makeIncreasing(numbers) = true.

By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

For numbers = [13, 31, 30], the output should be makeIncreasing(numbers) = false.

The initial array elements are not increasing.
By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
So, it's not possible to obtain a strictly increasing array, and the answer is false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer numbers

An array of non-negative integers.

Guaranteed constraints:
1 ≤ numbers.length ≤ 103,
0 ≤ numbers[i] ≤ 103.

[output] boolean

Return true if it is possible to obtain a strictly increasing array by applying the digit-swap operation at most once, and false otherwise.

'''
import itertools

def makeIncreasing(numbers):
    n = len(numbers)
    if n == 1:
        return True
    idx = -1
    count = 0
    for i in range(n-1):
        if numbers[i] >= numbers[i+1]:
            idx = i
            count+=1
            if count > 1:
                return False
    num = str(numbers[i])
    anses = list(itertools.permutations(num,len(num)))
    print(anses)
    for ans in anses:
        if i == 0:
            if int("".join(ans)) < numbers[i-1]:
                return True
        else:
            if numbers[i-1]<int("".join(ans))< numbers[i+1]:
                return True
    return False 
                     
                     
if __name__ == '__main__':
    test1= [1, 5, 10, 20]
    test = [1,3,900,10]
    ans = makeIncreasing(test)
    print(ans)
    
    