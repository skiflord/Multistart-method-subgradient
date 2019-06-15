from buildHaar import haar
from statistics import *

#import random2

vec3_haar_carrier = []

def signf(number):
    if number > 0:
        return True
    else: 
        return False


def search_extremum_point_method (pos_in_exel, i, h, parameter_list = []):
    check_value_for_exremum_one = 28
    check_value_for_exremum_two = 46
    true_or_false = None
    cur_x = i # The algorithm starts at x=...
    Epsilon = 0.015 
    Gamma = 0.022   
    haar_length = h # haar carrier length
    change_sign = False # Show change sign or not
    dist = 6    # epsillon current value
    step = 0    # step of algorithm
    extremum_point = 0 # Point to extremum of function
    df_square = lambda point: haar(haar_length, point, parameter_list) # Haar square of function
    nx_point = lambda point, square: point + Gamma * square # next point
    #nx_point = lambda point, square: square - parameter_list[point] + 1 # next point

    #init block for start statement for our algorithm
    (_,_,haar_square) = df_square(cur_x)
    staticPosValue = haar_square
    temp_sign = signf(haar_square)
    prev_x = cur_x
    #print(haar_square)
    while Epsilon < dist:
        step = step + 1
        vec3_haar_carrier.append((cur_x,parameter_list[cur_x],haar_length))
        (_,_,haar_square) = df_square(cur_x)
        sign = signf(haar_square)
        if temp_sign != sign:
            change_sign = True
            if change_sign:
                if haar_length != 1:
                    haar_length = haar_length - 1

        
        prev_x = cur_x
        #print(nx_point(cur_x,haar_square))
        cur_x = round(nx_point(cur_x,haar_square))
        #print(cur_x,prev_x) 
        #print(haar_square) 
        extremum_point = cur_x
        dist = abs(haar_square/1000)
        # print_statistics_per_point(cur_x, prev_x, parameter_list[cur_x], haar_length, dist, change_sign, haar_square, step)
        # print_statistics_per_point_in_file(cur_x, prev_x, parameter_list[cur_x], haar_length, dist, change_sign, haar_square, step)
        # print(haar_square)

    if extremum_point == check_value_for_exremum_one or extremum_point == check_value_for_exremum_two:
        true_or_false = 1
    else:
        true_or_false = 0

    # print(dist)
    # print(haar_square)
    # print_statistics_extremum_point(parameter_list[extremum_point], extremum_point, dist)
    # print_statistics_extremum_point_in_file(parameter_list[extremum_point], extremum_point, dist)
    #print_statistics_table_in_file(pos_in_exel, i,cur_x, h, Epsilon, dist, step, haar_length, staticPosValue, haar_square, true_or_false)
    # print(cur_x, h, Epsilon, dist, step)
    return (extremum_point, vec3_haar_carrier)

