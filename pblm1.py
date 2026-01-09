#1.Given an string, write a program to verify whether the string has equal number ofvowels and consonants or not
def equal_vowels_and_consonants_one_way(s):#less efficient than second way
    vowels=0
    vow="aeiouAEIOU"
    consonants=0
    wd=s.split()
    for i in wd:
        for j in i:
            if j.isalpha():
                if j in vow:
                    vowels+=1
                else:
                    consonants+=1
    if vowels==consonants:
        return True
    else:
        return False
def equal_vowels_and_consonants_second_way(s):
    vowels=set("aeiouAEIOU")
    vow,cons=0,0
    for i in s:
        if i.isalpha() and i in vowels:
            vow+=1
        elif i.isalpha() and i not in vowels:
            cons+=1
    if vow==cons:
        return True
    else:   
        return False
