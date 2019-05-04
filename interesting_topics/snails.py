'''
rray = [[1,2,3,4]，
         [8,9,4,7],
         [7,6,5,9],
         [4,3,5,1]
snail(array)＃=> [1,2,3,4,7,9,1,5,3,4,7,8,9,4,5,6]

'''
import numpy as np
def snails(input_n_n_list):
    snails_list = []
    np_input_list = np.array(input_n_n_list)
    while len(np_input_list) >0:
        snails_list += (np_input_list[0].tolist())
        ## Use + to combine the two list, but not append. 
        np_input_list = np.rot90(np_input_list[1:])
    return snails_list

print(snails([[1,2,3],[4,5,6],[7,9,0]]))

