import numpy as np

# Test element-wise for complex numbers and real numbers in a given array
def test_complex_real(array):
    is_complex = np.iscomplexobj(array)
    is_real = np.isrealobj(array)
    return is_complex, is_real

# Test if a given number is of a scalar type
def test_scalar(number):
    is_scalar = np.isscalar(number)
    return is_scalar

# Test complex and real numbers in an array
array = np.array([1+2j, 3, 4.5, 5+6j])
is_complex, is_real = test_complex_real(array)
print("Array:", array)
print("Complex numbers in the array:", is_complex)
print("Real numbers in the array:", is_real)

# Test if a number is a scalar type
number = 10
is_scalar = test_scalar(number)
print("Number:", number)
print("Is a scalar:", is_scalar)