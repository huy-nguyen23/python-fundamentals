def count_developers(lst):
    count=0
    for x in lst:
        if x.get('continent')=='Europe'and x.get('language')=='JavaScript':
            count+=1
    return count