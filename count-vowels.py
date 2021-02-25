# count-vowels.py

# Solution 1

def VowelCount(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([ch for ch in str_ if ch.lower() in vowels])
  
# Solution 2
# Using the lamba 

def VowelCount2(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len(filter(lambda x: x.lower() in vowels, str_))


print VowelCount(raw_input())
