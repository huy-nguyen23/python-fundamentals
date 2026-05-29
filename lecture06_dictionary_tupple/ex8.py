def is_same_language(lst): 
    language=lst[0].get('language')
    for x in lst:
        if x.get('language')!=language:
            return False
    return True