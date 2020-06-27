"""
Purpose :  Define a function that chooses the best designs of alpha_b
and alpha_p parameters based on the most external biofuel product.  
The function chooses a best design based on threshold criteria and a poor 
design based only on output measures.  
    
Created on 30/4/2020

@author: Murray Keogh

Program description: 
    Define a function that chooses the best designs of alpha_b
    and alpha_p parameters based on the most external biofuel product. The
    poor design finds the alpha_b and alpha_p values that result in the 
    max external biofuel product with no constraints. The best design
    defines thresholds for internal fuel and oscillation size and then chooses
    the alpha_b and alpha_p that result in the max external biofuel product
    that also satisfies the constraints. 
    
    
Data dictionary:
    
   Inputs:
       
   THRESHOLD_MAX_INTERNAL_FUEL : given value for max internal fuel
   THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL :given value for max oscillation size
   alpha_b_array                :given array of alpha_b values
   alpha_p_array                :calculated array of alpha_p values
   max_internal_biofuel         :array of max internal biofuel values
   oscillation_internal_biofuel :array of oscillation size values
   final_external_biofuel       :array of final external biofuel values
    
   Outputs:
   best_alpha_b            :alpha_b value for best design
   best_alpha_p            :alpha_p value for best design
   poor_alpha_b            :alpha_b value for poor design
   poor_alpha_p            :alpha_p value for poor design
           
   
   Other:
   max_biofuel              :maximum external biofuel value
   acceptable_index_array   :boolean array,whether threshold criteria are met
   acceptable_biofuel_array :array,external biofuel values for acceptable designs
   max_acceptable_biofuel   :maximum external biofuel value for acceptable designs
   
"""
import numpy as np

def design(THRESHOLD_MAX_INTERNAL_FUEL, THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL, 
alpha_b_array, alpha_p_array, max_internal_biofuel, oscillation_internal_biofuel, final_external_biofuel) :
    
    #poor design
    
    #find maximum external biofuel value
    max_biofuel = np.amax(final_external_biofuel)
    
    #find alpha_b index of the maximum external biofuel value
    poor_alpha_b = alpha_b_array[np.where(final_external_biofuel==max_biofuel)[0][0]]
    #find alpha_p index of the maximum external biofuel value
    poor_alpha_p = alpha_p_array[np.where(final_external_biofuel==max_biofuel)[1][0]]

    #best design
    
    #create boolean array where both internal and oscillation criteria are met    
    acceptable_index_array = (max_internal_biofuel <= THRESHOLD_MAX_INTERNAL_FUEL) \
    & (oscillation_internal_biofuel <= THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL)
    
    #create zero numpy array to store max external biofuel amounts
    acceptable_biofuel_array = np.zeros_like(final_external_biofuel)
    
    #update max external biofuel amounts where conditions are met
    acceptable_biofuel_array[acceptable_index_array] = final_external_biofuel[acceptable_index_array]
    
    #find the max external biofuel amount
    max_acceptable_biofuel = np.amax(acceptable_biofuel_array)
    
    #find alpha_b index of the maximum external biofuel value
    best_alpha_b = alpha_b_array[np.where(acceptable_biofuel_array==max_acceptable_biofuel)[0][0]]
    #find alpha_p index of the maximum external biofuel value
    best_alpha_p = alpha_p_array[np.where(acceptable_biofuel_array==max_acceptable_biofuel)[1][0]]
    
    return best_alpha_b,best_alpha_p,poor_alpha_b,poor_alpha_p
