
def buildplot(length_carrier, step, parameter_list = []):
    for i in range(length_carrier):
        parameter_list.insert(0,0)
        parameter_list.append(0)


    length = range(len(parameter_list))
    data = []
    for index in length[length_carrier:-length_carrier:step]:
        data.append(abs(haar_with_square(length_carrier, index, parameter_list)))
        #print(data)
        #(_,_,summary_square) = haar(length_carrier, index, parameter_list)
        #print(summary_square)
    #print(data)
    return data

def haar(length_carrier, position, parameter_list = []):
    carrier_left = 0
    carrier_right = 0
    summary_square =0
    #print(parameter_list)
    for elm in range(1,length_carrier+1):
        carrier_left += parameter_list[position - elm]*-1
        #print( position - elm)
    #print(carrier_left)


    for elm in range(1,length_carrier+1):
        carrier_right += parameter_list[position + elm - 1] # - 1 if middle haar not null 
        #print(carrier_right, elm)

    summary_square = carrier_left + carrier_right
    return (carrier_left,carrier_right,summary_square)


def haar_with_square (length_carrier, position, parameter_list = []):
    (carrier_left,carrier_right,_) = haar(length_carrier, position, parameter_list)
    carrier_left = carrier_left**2
    carrier_right = carrier_right**2
    #print(carrier_left, carrier_right)

    square = carrier_left + carrier_right
    
    #print(square)
    return square