def create_dict(keys, values):
    dicts={}
    for i in range(len(keys)):
        k=keys[i]

        if i>=len(values):
            v=None
        else:
            v=values[i]
        dicts[k]=v
    return dicts