def Palindrome(str_):
    cmp_str = str_.replace(" ", "")
    return cmp_str == cmp_str[::-1] and "true" or "false"


def Palindrome2(str_):
    cmp_str = ''.join(str_.split())
    return 'true' if cmp_str == ''.join(reversed(cmp_str)) else 'false'


print Palindrome(raw_input())
