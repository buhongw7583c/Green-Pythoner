
def get_divides(input_number):
    result_divides=[i for i in range (1, input_number+1)\
                      if (input_number % i ==0) 
                    ]
    return result_divides
   
def get_sum_squares(input_number, input_divides,result_squares):
    sum = 0
    for i in input_divides:
        sum = sum + i*i
    result_squares[input_number]=sum
    return result_squares

import math
def if_around(input_squares):
    return math.sqrt(input_squares).is_integer()
'''
Use the dictionary to contain the number and its corrsponding squares, 
saves space and time
'''
def all_around(start_num, end_num):
    all_arounds = []
    sum_squares = {}
    for i in range(start_num, end_num+1):
        divides = []
        divides = get_divides(i)
        #print (divides)
        sum_squares = get_sum_squares(i, divides, sum_squares)
        #print (sum_squares)
        if if_around(sum_squares[i]):
            all_arounds.append([i, sum_squares[i]])

    print (all_arounds)

all_around(1,1000)