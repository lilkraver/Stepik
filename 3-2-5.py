def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key*2 in d:
        d[key*2].append(value)
    else:
        d[key*2]=[]
        d[key*2].append(value)
    return   
