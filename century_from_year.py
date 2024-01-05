def century(year):
    # 2000 -> 20
    # 2001 -> 21
    # 1999 -> 20
    if year%100 == 0:
        return year//100
    else:
        return (year//100)+1