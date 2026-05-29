def count_languages(lst): 
    dicts={}
    count=0
    for x in lst:
        language=x.get('language')
        dicts[language]=dicts.get(language,0)+1
    return dicts