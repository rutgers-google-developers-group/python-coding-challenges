def LetterCapitalize(str):
    return " ".join(word.capitalize() for word in str.split())

print LetterCapitalize(raw_input())
