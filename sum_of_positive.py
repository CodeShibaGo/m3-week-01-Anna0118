def positive_sum(arr):
    sum=0
    if len(arr)==0:
        return 0
    else:
        for i in arr:
            if i>=0:
                sum+=i
    return sum
