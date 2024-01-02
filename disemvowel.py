def disemvowel(s):
    vowel='aeiouAEIOU'
    new_s=''
    for i in s:
        if i not in vowel:
            new_s+=i
    return(new_s)
