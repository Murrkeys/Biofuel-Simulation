"""
Purpose :  Define a function that can be used to simulate the biofuel
production process.

    
Created on 30/4/2020

@author: Murray Keogh

Program description: 
    Write a function that calculates the five differential calculations that
    make up the mathematical model for the biofuel production process. The
    output is five arrays that are the key measures for modeling this 
    process. 
    
    
Data dictionary:
    
   Inputs:
   data_set_to_use        : (integer) Set id for system constants needed for 
                            simulation
   array_time             : (array) An array of uniformly distributed time
                           instances 
   init_bacteria_amount   :The initial amount of bacteria
   alpha_b                : Value of the parameter alpha_b which is the
                           production rate of biofuel 
   alpha_p                : Value of the parameter alpha_p whihc is the
                           production rate of efflux pumps

   Outputs:
   array_bacteriaAmount    :(array) Amount of Bacteria
   array_sensor            :(array) Sensor output
   array_pump              :(array) Number of efflux pumps
   array_biofuelInt        :(array) Amount of biofuel inside bacteria
   array_biofuelExt        :(array) Amount of biofuel outsie of bacteria 
   
   Other:
   len_time_array          :length of the input time array
   dt                      :scalar value of step between time periods
   log_growth_rate         :log growth rate calculation 
   fuel_death_rate         :fuel death rate calculation
   pump_death_rate         :pump death rate calculation
   biofuel_prod_rate_denom :biofuel production rate denominator calculation
   pump_deg_rate           :pump degradation rate calculation
   
"""
import biofuel_system_parameter_sets as bsps
import numpy as np


def sim_biofuel(data_set_to_use, time_array, init_bacteria_amount, alpha_b, alpha_p) : 

    # BEGIN - DO NOT REMOVE 
    # Note: Please do not remove this
    sys_para = bsps.biofuel_system_parameter_sets(data_set_to_use)
    ALPHA_N = sys_para['ALPHA_N' ]  # Growth rate (1/h)
    ALPHA_R = sys_para['ALPHA_R' ]  # Basal repressor production rate (1/h)
    BETA_R =  sys_para['BETA_R']    # Repressor degradation rate (1/h)
    BETA_P =  sys_para['BETA_P']    # Pump degradation rate (1/h) 
    DELTA_N = sys_para['DELTA_N']   # Biofuel toxicity coefficient (1/(Mh))
    DELTA_B = sys_para['DELTA_B']   # Biofuel export rate per pump (1/(Mh))
    GAMMA_P = sys_para['GAMMA_P']   # Pump toxicity threshold 
    GAMMA_I = sys_para['GAMMA_I']   # Inducer saturation threshold (M)
    GAMMA_R = sys_para['GAMMA_R']   # Repressor saturation threshold 
    K_R  =    sys_para['K_R']       # Repressor activation constant (h)
    K_P  =    sys_para['K_P']       # Pump activation constant (1/h)
    K_B  =    sys_para['K_B']       # Repressor deactivation constant (1/M)
    V    =    sys_para['V']         # Ratio of intra to extracellular volume 
    I    =    sys_para['I']         # Amount of inducer             
    # The above lines set the following constants: 
    # ALPHA_N ALPHA_R BETA_R  BETA_P  DELTA_N DELTA_B GAMMA_P GAMMA_I 
    # GAMMA_R K_R K_P K_B V I       
    # END - DO NOT REMOVE    

    
    # You should put your work below this line 
    
    # Extract information from time vector 
    len_time_array = len(time_array)  # number of time points
    dt = time_array[1]-time_array[0]  # time increment
    
    
    # Initialise storage for positions and velocities
    array_bacteriaAmount = np.zeros_like(time_array)
    array_sensor  = np.zeros_like(time_array)
    array_pump   = np.zeros_like(time_array)
    array_biofuelInt = np.zeros_like(time_array)
    array_biofuelExt = np.zeros_like(time_array)
    
    # Initialise bacteria amount
    array_bacteriaAmount[0] = init_bacteria_amount
    
     # the simulation loop
    for k in range(1,len_time_array): 
        # Update bacteria amount array
        
        #calculate complex rates for ease of reading
        
        log_growth_rate = ALPHA_N*array_bacteriaAmount[k-1]* \
                          (1-array_bacteriaAmount[k-1])
        
        fuel_death_rate = DELTA_N*array_biofuelInt[k-1]*array_bacteriaAmount[k-1]
        
        pump_death_rate = ALPHA_N*array_bacteriaAmount[k-1]*array_pump[k-1]/ \
                          (array_pump[k-1]+GAMMA_P)
                          
        biofuel_prod_rate_denom = (array_sensor[k-1]/ \
                                  (1+K_B*array_biofuelInt[k-1]))+GAMMA_R
        
        pump_deg_rate = BETA_P*array_pump[k-1]
        
        #Update bacteria amount array
        array_bacteriaAmount[k] = array_bacteriaAmount[k-1]+(log_growth_rate - \
        fuel_death_rate - pump_death_rate)*dt; 
        
         # Update sensor array
        array_sensor[k] = array_sensor[k-1] + \
        (ALPHA_R + K_R*(I/(I+GAMMA_I))-BETA_R*array_sensor[k-1])*dt;
        
        # Update pump array
        array_pump[k] = array_pump[k-1] + (alpha_p + K_P/biofuel_prod_rate_denom - \
        pump_deg_rate)*dt;
        
        
        # Update biofuel internal array
        array_biofuelInt[k] =  array_biofuelInt[k-1] + \
        ((alpha_b*array_bacteriaAmount[k-1])-(DELTA_B*array_pump[k-1]* \
        array_biofuelInt[k-1]))*dt;
         
        # Update biofuel external array
        array_biofuelExt[k] =  array_biofuelExt[k-1] + \
        (V*DELTA_B*array_pump[k-1]*array_biofuelInt[k-1]* \
        array_bacteriaAmount[k-1])*dt;
         
         #return five output arrays
    return array_bacteriaAmount,array_sensor,array_pump,array_biofuelInt,array_biofuelExt
         
         
        
        
        
        
        
        
        
        
        
        
        




