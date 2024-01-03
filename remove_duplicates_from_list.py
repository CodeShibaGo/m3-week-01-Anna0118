def distinct(seq):
    # 原本還想複製陣列來做檢查和移除，但會遇到index超出範圍的問題
    # 原來陣列也可用in來掃描，以及用append方式，以及去比對
    result=[]
    for i in seq:
        if len(result)==0 or i!=result[-1]:
            result.append(i)
    return result
