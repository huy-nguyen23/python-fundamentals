def duplicate_count(text):
    count=0
    dicts={}
    for i in text.lower():
        if i not in dicts:
            dicts[i]=1
        else:
            dicts[i]+=1
    for j in dicts:
        if dicts[j]>=2:
            count+=1
    return count