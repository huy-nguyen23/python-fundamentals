def ordered_count(inp):
    dict={}
    array=[]
    for x in inp:
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1
    for y in dict:
        t=(y,dict[y])
        array.append(t)
    return array