'''
You are given numbers, a 3 × n matrix which contains only digits from 1 to 9. Consider a sliding window of size 3 × 3, 
which is sliding from left to right through the matrix numbers. The sliding window has n - 2 positions when sliding through the initial matrix.

Your task is to find whether or not each sliding window position contains all the numbers from 1 to 9 (inclusive). Return an array of length n - 2, 
where the ith element is true if the ith state of the sliding window contains all the numbers from 1 to 9, and false otherwise.

Example

numbers = [[1, 2, 3, 2, 5, 7],
           [4, 5, 6, 1, 7, 6],
           [7, 8, 9, 4, 8, 3]]

the output should be isSubmatrixFull(numbers) = [true, false, true, false].
Let's consider all sliding window states:

    The 1st state contains all digits from 1 to 9.
    The 2nd state doesn't contain digit 7.
    The 3rd state contains all digits from 1 to 9.
    The 4th state doesn't contain digit 9.
    Summary, there are four states of the sliding window, and the resulted array is [true, false, true, false].

Input/Output

    [execution time limit] 0.5 seconds (cpp)

    [input] array.array.integer numbers

    A matrix containing only digits from 1 to 9.

    Guaranteed constraints:
    numbers.length = 3,
    3 ≤ numbers[i].length ≤ 100,
    1 ≤ numbers[i][j] ≤ 9.

    [output] array.boolean

    Return an array of booleans as described above.

'''

def solve(mat):
    