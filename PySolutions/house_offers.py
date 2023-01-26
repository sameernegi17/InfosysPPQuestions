"""
You have a street of length N on the coordinate axis and want to sell
as much of it possible.

You are aware that the sale process is by selling a part of the 
street that starts at a starting point on the x-axis and ends at 
the end point on the x-axis between 1 to N.

You receive Q offers where each offer is determined buyer's desire with 
the starting S, and ending E, point. 
A buyer always wants to buy the entire exclusively and does not agree to buy 
a part of it.

Assume that you choose a set of these offers so that you can sell the largest possible length of the street.
Your task is to find the  smallest length of the remaining street 
"""

from test_utils.helper_functions import verify_output


def find_offers(input):
    pass


if __name__ == "__main__":
    verify_output(2, find_offers([5, 3, 1, 2, 3, 3, 4, 5]))
    verify_output(2, find_offers([9, 3, 1, 4, 2, 6, 9, 8]))
    verify_output(0, find_offers([10, 3, 1, 2, 6, 5, 9, 10]))
