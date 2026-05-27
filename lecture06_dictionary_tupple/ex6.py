def get_first_python(users):
    for x in users:
        fName=x.get('first_name')
        cTry=x.get('country')
        if x.get('language')=='Python':
            return f'{fName}, {cTry}'
    return 'There will be no Python developers'