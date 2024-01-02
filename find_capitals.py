def find_capitals(word):
    ls=[]
    for i in word:
        if i == i.upper() and i.isalpha():
            ls.append(i)
    return ''.join(ls)

# def find_capitals(word):
#     ls = ''
#     for i in word:
#         if i.isupper():
#             ls += i
#     return ls

