"""
Purpose :  Define a function that uses many different pairs of alpha_b
and alpha_p to simulate the biofuel production.
    
Created on 30/4/2020

@author: Murray Keogh

Program description: 
    Write a function that uses many different pairs of alpha_b
    and alpha_p to simulate the biofuel production.  The output is five arrays
    with each entry being the output measure value at a specific alpha_b and 
    alpha_p value.  
    
    
Data dictionary:
    
   Inputs:
   data_set_to_use         :given data set to use for simulation
   time_array              :given array of time to simulate over
   INITIAL_BACTERIA_AMOUNT :given initial amount of bacteria
   alpha_b_array           :given array of alpha_b values
   ALPHA_P_LOWER           :given beginning value of alpha_p
   ALPHA_P_UPPER           :given ending value of alpha_p
   ALPHA_P_STEP            :given step size to evaluate alpha_p
    
   Outputs:
   alpha_b_array                :given array of alpha_b values
   alpha_p_array                :calculated array of alpha_p values
   max_internal_biofuel         :array of max internal biofuel values
   oscillation_internal_biofuel :array of oscillation size values
   final_external_biofuel       :array of final external biofuel values
            
   
   Other:
   len_alpha_b_array        :length of the input alpha_b array
   len_alpha_p_array        :length of the input alpha_p array
   len_time_array           :length of the input time array
   alpha_b                  :alpha_b value each simulation
   alpha_p                  :alpha_p value each simulation
   
"""

import numpy as np
import sim_biofuel as sb
import find_max_and_oscillation as fmo

def generate(data_set_to_use, time_array, INITIAL_BACTERIA_AMOUNT, alpha_b_array, ALPHA_P_LOWER, ALPHA_P_UPPER, ALPHA_P_STEP) :
    
    #create alpha_p array using the given lower,upper, and step values
    alpha_p_array = np.arange(ALPHA_P_LOWER,ALPHA_P_UPPER+ALPHA_P_STEP, ALPHA_P_STEP)
    
    #create length value for matrix initialization
    len_alpha_b_array = len(alpha_b_array)
    len_alpha_p_array = len(alpha_p_array)
    len_time_array = len(time_array)
    
    #iniatilize internal, oscillation, and external biofuel arrays
    max_internal_biofuel = np.zeros((len_alpha_b_array,len_alpha_p_array))
    oscillation_internal_biofuel = np.zeros((len_alpha_b_array,len_alpha_p_array))
    final_external_biofuel = np.zeros((len_alpha_b_array,len_alpha_p_array))
    
    
    #loop through alpha_b and alpha_p arrays
    for i in range(0,len(alpha_b_array)):
        for j in range(0,len(alpha_p_array)):
            
            #set alpha_b and alpha_p values
            alpha_b = alpha_b_array[i]
            alpha_p = alpha_p_array[j]
            
            #simulation
            bacteria_amount_array,sensor_array,pump_array,biofuel_int_array, \
            biofuel_ext_array = sb.sim_biofuel(data_set_to_use,time_array, \
            INITIAL_BACTERIA_AMOUNT,alpha_b,alpha_p)
            
            #find max and oscillation value
            max_internal_fuel, oscillation_internal_fuel = fmo.find_max_and_oscillation(biofuel_int_array) 
            
            #update internal biofuel matrix with maximum value
            max_internal_biofuel[i,j] = max_internal_fuel
            #update oscillation matrix with oscillation value
            oscillation_internal_biofuel[i,j] = oscillation_internal_fuel
            #update external biofuel matrix with last external value
            final_external_biofuel[i,j] = biofuel_ext_array[len_time_array-1]
            
    
    return alpha_b_array,alpha_p_array,max_internal_biofuel,oscillation_internal_biofuel,final_external_biofuel 
            
            
            
    
    