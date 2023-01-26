def verify_output(expected,actual):
    if expected == actual:
        print("Current Test Passed")
    else:
        print(f"Failed Actual : {actual} not equal to Excpected : {expected}")
