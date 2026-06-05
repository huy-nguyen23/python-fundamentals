def calculate_area(length,width):
    if length<=0 or width<=0:
        raise ValueError('Dimensions must be positive')
    else:
        area=length*width
        return area

try:
    area= calculate_area(5,-2)
    print('Area:',area)
except ValueError as e:
    print('Error calculating area:',e)


try:
    area= calculate_area(5,10)
    print('Area:',area)
except ValueError as e:
    print('Error calculating area:',e)
    
    
    
    
    
    #      git add .
    #      git commit-m 'python exercise 3 lecture 07'
   #       git push