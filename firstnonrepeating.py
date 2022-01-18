# Write a function that takes a string input, and returns
# the first character that is not repeated anywhere in the string.

def first_non_repeating_letter(string):
    tes = string.lower()
    a = ''
    for i in tes:
        if tes.count(i) == 1:
            a = i
            return string[tes.index(a)]
    return a


first_non_repeating_letter("aasssddeeefaggtyyyuu")
