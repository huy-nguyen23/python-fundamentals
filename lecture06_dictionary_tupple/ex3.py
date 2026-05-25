def user_contacts(data):
    dicts={}
    for x in data:
        name=x[0]
        if len(x)==2:
            code=x[1]
        else:
            code=None
        dicts[name]=code
    return dicts