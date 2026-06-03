def divide_numbers(numerator,denominator):
    try:
        result= numerator/denominator
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        return None
    except TypeError:
        print('Error: Both inputs must be numbers.')
        return None
    else:
        print(f'The result is {result}')
        return result
divide_numbers(10,2)
divide_numbers(10,0)
divide_numbers(10,'a')