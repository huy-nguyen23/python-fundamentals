def find_senior(lst): 
    ageMax=0
    array=[]
    for x in lst:
        if ageMax<x.get('age'):
            ageMax=x.get('age')
            array=[x]
        elif ageMax==x.get('age'):
            array.append(x)
    return array