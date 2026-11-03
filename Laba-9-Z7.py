def filter_list(items):
    result=[]
    for item in items:
        if isinstance(item, int) and item >=0:
            result.append(item)
            
    return result