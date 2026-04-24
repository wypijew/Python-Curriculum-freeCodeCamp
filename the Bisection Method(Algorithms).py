
def square_root_bisection(number, tolerance = 1e-7, max_iterations = 1000):

    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    if 0 < number < 1:
        low = 0
        high = 1
    else:
        low = 0
        high = number
        
    iterations = 0    

    while iterations < max_iterations:
        mid = (low + high) / 2
        square = mid * mid

        if abs(high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        if square < number:
            low = mid
        else:
            high = mid

        iterations += 1

    print(f"Failed to converge within {max_iterations} iterations")
    return None 
    
print(square_root_bisection(0))