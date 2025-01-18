from itertools import chain
 
nums = [[1, 2, 3],
            [3, 6, 7],
            [7, 5, 4]]
             

print ("initial list ", nums)
 

flatten_list = list(chain.from_iterable(nums))
 

print ("final_result", flatten_list)