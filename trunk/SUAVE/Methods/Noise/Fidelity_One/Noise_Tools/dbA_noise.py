# dbA_noise.py
# 
# Created:  Jul 2015, C. Ilario
# Modified: Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import autograd.numpy as np 

# ----------------------------------------------------------------------
#  dbA Noise
# ----------------------------------------------------------------------

def dbA_noise(SPL):
    """This method calculates de A-weighted level from a 1/3 octave band noise spectra

        Inputs:
                    SPL     - Sound Pressure Level in 1/3 octave band

                Outputs: [dB]
                    SPL_dbA - A-weighted Sound Pressure Level in dbA"""
    
    #Matrix with the dbA attenuation factor for each octave band frequnecy ranging from 50Hz to 10000Hz
    dbA_attenuation = np.array((-30.2,-26.2,-22.5,-19.1,-16.1,-13.4,-10.9,-8.6,-6.6,-4.8,-3.2,-1.9,-0.8,0,0.6,1,1.2,1.3,1.2,1,0.5,-0.1,-1.1,-2.5))
    
    #Calculation the SPL_dbA
    SPL_dbA = SPL+dbA_attenuation
        
    return (SPL_dbA)