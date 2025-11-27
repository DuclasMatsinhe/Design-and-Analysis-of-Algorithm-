def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i  # starting index of match
    return -1

text = "AABAACAADAABAABA"
pattern = "AABA"
print("Naive Match Index:", naive_string_match(text, pattern))
