
# Change the array to flat list
list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [k for i in list_ for k in i] #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print (new_list)

import numpy as np
print (np.r_[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#rotate list, change from line to column, but the result is a zip object
#the returned object is tuple

line_to_columnn_list = list(zip(*list_))
print(line_to_columnn_list)

#use the NP rotate method to rotate 90 degree
np_list = np.array(list_)
roate_np_list = np.rot90(np_list)
roate_np_list =np.rot90(roate_np_list)
print(roate_np_list)