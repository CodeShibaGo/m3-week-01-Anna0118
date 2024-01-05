def count_duplicates(text):

    if len(text)==0:
        return len(text)
    result={}
    count=0
    for i in text.lower():
        #aabbcde, 2
        #AaBbcde, 2
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    for key in result:
        if result[key]>1:
            count+=1
    return count
