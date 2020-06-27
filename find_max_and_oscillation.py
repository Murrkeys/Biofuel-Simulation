"""
Purpose :  Define a function that finds the maximum amount of internal
biofuel and the amount of oscillation in the level of internal biofuel.
    
Created on 30/4/2020

@author: Murray Keogh

Program description: 
    Write a function that finds the maximum value and its indices in the 
    input array. The function then finds the minimum value at an index after
    the maximum value.  The oscillation is calculated by subtracting the 
    minimum from the maximum. The output is the maximum value and 
    the calculated oscillation size. 
    
    
Data dictionary:
    
   Inputs:
   input_array         :(array) given input array

   Outputs:
   max_value           :maximum amount of internal biofuel
   oscillationSize     :oscillation size
   
   Other:
   len_input_array         :length of the input array
   max_value_index         :index of the maximum value
   min_biofuel_int         :minimum value after the maximum value
   
"""
import numpy as np

def find_max_and_oscillation(input_array):
    
    #create length value 
    len_input_array = len(input_array)
    
    #find max value of input array
    max_value = np.max(input_array)
    #find index of max value in input array
    max_value_index = np.where(input_array==max_value)[0][0]
    
    #if max value is at last index, set oscillation size to zero
    if max_value_index == len_input_array-1:
        oscillationSize = 0
    
    else:
        #find the next minimum value after the max value
        min_biofuel_int = np.min(input_array[max_value_index:])
        #calculate oscillation size
        oscillationSize = max_value - min_biofuel_int
        
    #return output
    return max_value, oscillationSize
   