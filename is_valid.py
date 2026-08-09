def is_valid(s):
    opened = []
    collections = {'()', '[]', '{}'}
    for el in s:
        if el in '([{':
            opened.append(el)
        else:
            if opened:
                last_opened = opened.pop()
                if f"{last_opened}{el}" not in collections:
                    return False
            else:
                return False

    return len(opened) == 0


print(is_valid(s = "{[]}"))
