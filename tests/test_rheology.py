"""
Tests for the rheology module
"""

import pytest
import numpy as np

# Import our rheology code
import sys
sys.path.append('.')  # This helps Python find our modules
from src.fluids.rheology import BinghamPlasticModel

def test_bingham_plastic():
    """
    Test the Bingham Plastic model calculations
    """
    # Create a mud with:
    # - Plastic viscosity: 15 cP = 0.015 Pa·s
    # - Yield point: 10 lb/100ft² = about 5 Pa
    model = BinghamPlasticModel(plastic_viscosity=0.015, yield_point=5.0)
    
    # Test 1: At zero shear rate, stress should equal yield point
    stress = model.shear_stress(0)
    print(f"At shear rate 0: stress = {stress} Pa")
    assert stress == 5.0, f"Expected 5.0, got {stress}"
    
    # Test 2: At 100 s⁻¹, stress should be yield point + viscosity * shear rate
    stress = model.shear_stress(100)
    expected = 5.0 + 0.015 * 100  # 5.0 + 1.5 = 6.5
    print(f"At shear rate 100: stress = {stress} Pa, expected = {expected} Pa")
    assert stress == expected, f"Expected {expected}, got {stress}"
    
    print("All tests passed! ✅")

# This runs the test
if __name__ == "__main__":
    test_bingham_plastic()