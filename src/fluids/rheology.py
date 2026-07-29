"""
Drilling Fluids Rheology Module
This calculates how drilling mud flows
"""

import numpy as np

class BinghamPlasticModel:
    """
    This is a simple model for drilling mud behavior
    It helps us calculate pressure drops
    """
    
    def __init__(self, plastic_viscosity, yield_point):
        """
        Sets up the mud properties
        
        Args:
            plastic_viscosity: How thick the mud is (in Pa·s)
            yield_point: How much force needed to start flow (in Pa)
        """
        self.pv = plastic_viscosity
        self.yp = yield_point
    
    def shear_stress(self, shear_rate):
        """
        Calculates the shear stress at a given shear rate
        
        Formula: τ = τ_y + μ_p × γ
        
        Args:
            shear_rate: How fast the mud is being sheared (1/s)
            
        Returns:
            Shear stress in Pascals (Pa)
        """
        return self.yp + self.pv * shear_rate
    
    def effective_viscosity(self, shear_rate):
        """
        Calculates the apparent viscosity at a given shear rate
        
        Args:
            shear_rate: How fast the mud is being sheared (1/s)
            
        Returns:
            Effective viscosity in Pa·s
        """
        if shear_rate <= 0:
            return float('inf')  # Can't divide by zero
        return self.shear_stress(shear_rate) / shear_rate