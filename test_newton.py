import pytest
import numpy as np
import math

import newton

# # Important: structure of tests assumes a dictionary with an 'x'
# # key as the output. 

def test_basic_function():
    assert np.isclose(newton.optimize(4), 1)

def test_bad_input():
    with pytest.raises(TypeError):   
        newton.optimize(4)

