def array_diff(a, b):
    if len(a)==0:
        return []
    result=[]
    # a=[1,2,2], b=[1], result=[2,2]
    for i in range(len(a)):
        if a[i] not in b:
            result.append(a[i])
    return result