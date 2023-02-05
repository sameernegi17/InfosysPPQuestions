#ifndef GUARD_F0368418_EBE2_453C_A5D1_AB243D5F3CD8
#define GUARD_F0368418_EBE2_453C_A5D1_AB243D5F3CD8
"""
You are given an array A of length N and an integer K.
 It is given that a number m is called special if gcd(m,Aj) = 1 for all 0<=j<N.

 

Let R be an array containing all special numbers in the range [1, K] 
in sorted order. Your task is to return R.

 

Note:

·       A follows 0-based indexing.
"""

from test_utils.helper_functions import verify_output
from collections import Counter

def find_gcd(input_array):
    _ = input_array[0]
    max_limit = input_array[1]
    input = input_array[2:]
    gcd_array = [N for N in range(1,max_limit+1)]
    c = Counter(input)

    for x in c:
        if x > max_limit:
            break

        if x != 1:
            for index in range(x-1,max_limit,gcd_array[x-1]):
                gcd_array[index] = -1

    out = []
    for item in gcd_array:
       if item != -1:
           out.append(item)

    return out


if __name__ == "__main__":
    verify_output([1,5], find_gcd([3,5,1,2,3]))
    verify_output([1,2,4], find_gcd([4,5,3,3,5,7]))
    verify_output([1], find_gcd([4,1,1,1,1,1]))


#endif /* GUARD_F0368418_EBE2_453C_A5D1_AB243D5F3CD8 */
