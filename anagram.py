# implementation of hash table
# dictionary in python is a hash table

def is_it_anagrams(str1, str2):
    freq1 = {}
    freq2 = {}
    for ch in str1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in str2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for key, value in freq1.items():
        if key not in freq2 and freq2[key] != value:
            return False
    return True


if __name__ == "__main__":
    print(is_it_anagrams("randi", "ra nd i"))
