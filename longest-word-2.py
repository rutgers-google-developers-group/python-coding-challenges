  
def LongestWord(sen):
    longest = ""
    for word in sen.split():
        if word.isalpha():
            #if re.match('^[\w-]+$', word):
            longest = word if len(word) > len(longest) else longest
    return longest


def LongestWord2(sen):
    return max(filter(lambda x: x.isalpha(), sen.split()), key=len)


# keep this function call here
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())
