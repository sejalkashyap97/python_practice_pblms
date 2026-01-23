# Write a program to crop out the words that are palindromes from a sentence given
# as user input
def is_palindrome(wd):
    if wd==wd[::-1]:
        return True
    else:   
        return False
def removing_palindrome(sentence):
    word=sentence.split()
    for i in word: 
        if is_palindrome(i):
            sentence=sentence.replace(i,"")
    return sentence

