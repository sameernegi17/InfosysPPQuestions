from test_utils.helper_functions import verify_output

def subArrayExists(arr, N):
    # traverse through array
    # and store prefix sums
    n_sum = 0
    s = set()

    for i in range(N):
        n_sum += arr[i]

        if n_sum == 0 or n_sum in s:
            return i
        s.add(n_sum)    

    return False


def good_array(input):
    N = len(input)
    operation = 0
    index = subArrayExists(input, N)
    while index:
        input.insert(index,100)
        index = subArrayExists(input, len(input))
        operation +=1
   
    return operation


if __name__ == "__main__":
    verify_output(2, good_array([1,-1,1]))
    verify_output(0, good_array([-2,1,2,3]))
    verify_output(3, good_array([1,-1,1,2,-3]))
