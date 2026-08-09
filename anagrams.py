def is_anagram(s, t) -> bool:
    s_as_dict = {}
    if len(s) != len(t):
        return False
    for l in s:
        if l not in s_as_dict:
            s_as_dict[l] = 1
        else:
            s_as_dict[l] += 1

    for l in t:
        if l in s_as_dict:
            if s_as_dict[l] == 1:
                s_as_dict.pop(l)
            else:
                s_as_dict[l] -= 1

    return len(s_as_dict) == 0


print(is_anagram(s = "a", t = "ab"))