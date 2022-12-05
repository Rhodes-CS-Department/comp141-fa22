#!/usr/bin/env python
# coding: utf-8

# # Day 41: Binary Numbers
# 
# ### Solutions to Lab 11 Questions

# In[ ]:


from string import punctuation

#This function removes punctuation and changes s to it's lowercase version
#Parameters: s, a string
#Returns: a cleaned up version of s
def clean_string(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', punctuation))
    return s

def word_count(filename):
    word_counts = {}
    file = open(filename, 'r')
    for line in file:
        line = line.rstrip()
        #Need to call the clean_string function to clean up any punctuation in the string.
        line = clean_string(line)
        words = line.split()
        for i in range(len(words)):
            word = words[i]
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    file.close()
    return word_counts

grimm_counts = word_count('data/pg-grimm.txt')
print(grimm_counts['princess']) # prints 101
print(grimm_counts['prince']) # prints 63

holmes_counts = word_count('data/pg-sherlock_holmes.txt')
print(holmes_counts['sherlock']) # prints 102
print(holmes_counts['holmes']) # prints 463


# In[ ]:


def decode(cipher, n):
    cipher = cipher.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
  
    text = ''
    for i in range(0, len(cipher)):
        ch = cipher[i]
        if ch in alphabet:
            text += alphabet[(alphabet.index(ch) - n) % 26]
        else:
            text += ch
    return text

def main():

    file = open('data/cipherText.txt', 'r')
  
    #Need to keep track of the counts of all the letters in the encrypted message
    letterCnts = {}
    #Need to add together all the lines from the encrypted message, so you can 
    #pass the entire encrypted string into the decode function.
    text = ''
  
    for line in file:
        line = line.rstrip()
        text += line
        for i in range(len(line)):
            ch = line[i]
            if ch.isalpha():
                if ch in letterCnts:
                    letterCnts[ch] += 1
                else:
                    letterCnts[ch] = 1
    file.close()
  
    #Find the max letter in the letterCnts dictionary
    maxLetter = ''
    maxLetterCnt = 0
    for key in letterCnts:
        if letterCnts[key] > maxLetterCnt:
            maxLetterCnt = letterCnts[key]
            maxLetter = key
    print(maxLetter, maxLetterCnt)
  
    #Need to determine the difference between e and the max letter index
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #Find the index of the max letter in the alphabet
    maxLetterInd = alphabet.index(maxLetter)
    #Compare the index of the max letter to the index of e to get the shift
    shift = maxLetterInd - alphabet.index('e')
  
    #Call the decode function with the entire encrypted message and the shift that you just found
    text = decode(text, shift)
    print(text)

main()


# In[ ]:


# This function takes in two dictionaries d1 and d2 and returns a dictionary of word counts 
# (key = word, value = count), but only for words in d1 but not in d2.
def unique(d1, d2):
    counts = {}
    for key in d1:
        if key not in d2:
            counts[key] = d1[key]
    return counts

unique({'the': 7221, 'project': 88, 'gutenberg': 29, 'ebook': 10, 'of': 1488, 'by': 316, 'this': 375, 'is': 492, 'for': 772,},
       {'the': 1009, 'of': 988, 'by': 316, 'this': 375, 'is': 492, 'for': 772, 'at': 635, 'no': 321, 'and': 5546})


# # Binary Numbers
# 
# Back at the beginning of the semester, we talked a little bit about how all data in a computer is stored in sequences of 0s and 1s. We're going to spend some time today learning about binary numbers, since they are the underlying data representation.
# 
# __Byte:__ just enough memory to store letter or small number 
# * Divided into eight bits 
# * __Bit:__ electrical component that can hold positive or negative charge, like on/off switch 
# * The on/off pattern of bits in a byte represents data stored in the byte 
# 
# ### Binary Numbers
# A Binary Number is made up of only 0s and 1s.
# * Example: 110100 - There are no 2, 3, 4, 5, 6, 7, 8 or 9 in binary.
# * "There are 10 types of people in this world: those who understand binary and those who don't" - Unknown
# * "Binary is as easy as 1, 10, 11."
# 
# ### How do we count in binary?
# ![binary1.png](attachment:binary1.png)
# 
# 
# ### How do we count in decimal?
# ![binary2.png](attachment:binary2.png)
# 
# ### Applying to Binary
# ![binary3.png](attachment:binary3.png)

# |     Decimal:    |     0    |     1    |      2    |      3    |      4     |      5     |      6     |      7     |       8     |       9     |      10     |      11     |      12     |      13     |      14     |      15     |
# |:---------------:|:--------:|:--------:|:---------:|:---------:|:----------:|:----------:|:----------:|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
# |      Binary:    |     0    |     1    |     10    |     11    |     100    |     101    |     110    |     111    |     1000    |     1001    |     1010    |     1011    |     1100    |     1101    |     1110    |     1111    |
# 
# 
# |     Decimal:    |       20     |       25     |       30     |       40      |       50      |       100      |        200      |        500       |
# |:---------------:|:------------:|:------------:|:------------:|:-------------:|:-------------:|:--------------:|:---------------:|:----------------:|
# |      Binary:    |     10100    |     11001    |     11110    |     101000    |     110010    |     1100100    |     11001000    |     111110100 

# ## Converting Binary to Decimal
# 
# In the decimal system, each position in the number represents the value * 10^position.
# * Example: $193 = 1 * 10^2 + 9 * 10^1 + 3 * 10^0$
# 
# This is the same in binary, except since is a base-2 system, each position is 2^position.
# * $10111= 1 * 2^4 + 0 * 2^3 + 1 * 2^2 + 1 * 2^1  + 1 * 2^0$
# * $101001 = 1 * 2^5 + 0 * 2^4 + 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0$
# 
# ![binary4.png](attachment:binary4.png)

# Since it can be ambiguous which base system a number is representing, for example if I say 10 do I mean ten, or do I mean two in binary, we can decscribe a number by it's base. The notation for this is $value_{base}$.
# 
# ## Practice
# Convert $1010110_2$ into decimal

# ## Converting Decimal into Binary
# ![binary5.png](attachment:binary5.png)

# ## Practice
# Convert $39_{10}$ into binary
# 

# Please do the following:
# * Complete Project 8 - due by 11:59pm tomorrow
# * Study for final exam - practice problems and solutions on Canvas

# ## Final Exam Information
# 
# * 10AM class: Monday, December 12th from 8:30-11:00am in Briggs 019
# * 11AM class: Friday, December 9th from 1:00-3:30pm in Briggs 019
# * Noon class: Tuesday, December 13th from 1:00-3:30pm in Briggs 019
# * You may use the String, List and Dictionary Reference Handouts during the exam (will be provided for you).
# * You may NOT use any string, list, or dictionary methods that are not on the provided reference sheets. Doing so on any question that asks you to write some code will automatically reduce your grade in half on that question.

# In[ ]:




