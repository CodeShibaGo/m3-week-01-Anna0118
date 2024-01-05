def reverse_string(s):
    new_string=''
    for i in range(len(s)):
        new_string+=s[-(i+1)]
    return new_string

## 進階版
# def reverse_string(s):
#     return s[::-1]