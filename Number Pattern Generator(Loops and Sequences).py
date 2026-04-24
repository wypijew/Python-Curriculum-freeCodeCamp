
def number_pattern(n):
 
    numbers = []

    if not isinstance(n, int):
        return ('Argument must be an integer value.')
    
    if n < 1:
            return ('Argument must be an integer greater than 0.')  

    for i in range(1,n+1):
        numbers.append(str(i))
        result = ' '.join(numbers)

    return result

print(number_pattern(4))