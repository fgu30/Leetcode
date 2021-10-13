
def count_secret_pairs(
                       upperBound,
                        lowerBound,
                        consecutiveDifference) -> int:
    # Initial Variable Setting
    highest_sum = lowest_sum = sum = 0
    for value in consecutiveDifference:
        sum += value
        highest_sum = max(sum, highest_sum)
        lowest_sum = min(sum, lowest_sum)
    print(highest_sum,lowest_sum) # 3,10
    # Need to +1 because of combination  = difference +1 ( count of ([2,3,4,5]) = (5-2) +1)
    result = (upperBound - lowerBound + (lowest_sum - highest_sum + 1))
    if result < 0:
        # Correction suggestion from @rvlyanon, thanks!
        return 0
    else:
        return result
        
count_secret_pairs(3,10,[-2,-1,-2,5])