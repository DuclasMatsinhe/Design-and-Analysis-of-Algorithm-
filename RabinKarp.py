def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1) % q
    p_hash = 0
    t_hash = 0

    # Initial hash values
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide pattern over text
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + 1])) % q
            if t_hash < 0:
                t_hash += q

    return -1


text = "GEEKS FOR GEEKS"
pattern = "GEEK"
print("Rabin-Karp Match Index:", rabin_karp(text, pattern))
